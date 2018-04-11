import argparse
import json
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
import requests
import cv2
import numpy as np
import math
import os
import numpy as np
import util as ut
import svm_train as st 
import re
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import io, time
from flask_pymongo import PyMongo # PyMongo allows us to work directly with the mongo database without defining a schema. It is a wrapper for mongodb library in flask 
from werkzeug.security import generate_password_hash, check_password_hash # Using werkzeug library to encrypt user passwords




#cap = PiCamera(0)
app = Flask(__name__)

# Configurating our database with flask
app.config['MONGO_DBNAME'] = 'gesturebasedui' # 'weather' is our db name on mlab
# URI (Uniform Resource Locator) is supplied by mlab. This identifies and locates where the database is on mlab
app.config['MONGO_URI'] = 'mongodb://gesturebasedBT2:password@ds241489.mlab.com:41489/gesturebasedui'

mongo = PyMongo(app) # Initialise connection to mongo database.

# For setting the flags for app
FLAGS = None

# Get the current directory
cwd = os.getcwd();

# Home route
@app.route("/")
def index():
    # if username is logged in
    if 'username' in session:
        # flash a message to user to indicate they are logged in.
        flash("Logged in as " + session['username'])
        return render_template("index.html")
    else:
        return render_template("login.html")

# Registration
@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        users = mongo.db.Users # Accessing our users collections
        # Checking to see if a username already exist in the users collection
        existing_user = users.find_one({'name' : request.form['username']})

        # if theres no existing username
        if existing_user is None:
            # Generating sha256 hash from user password
            hashpass = generate_password_hash(request.form['pass'], method='sha256')
            # Add new user to users collection along with password
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            # Activate a session using that username
            session['username'] = request.form['username']
        # Once user is registered.. return login page for them to login
            return redirect(url_for('login'))
        else:
            error = 'Username already exists'
            #return redirect(url_for('register'))
            
        
    return render_template('register.html', error=error)

# Login
@app.route('/login', methods=['GET','POST'])
def login():
    error = None # error variable set to None as default.
    if request.method == 'POST':
        users = mongo.db.Users # access the users collection in the database
        # Checking to see if username exists
        login_user = users.find_one({'name' : request.form['username']})

        if login_user: # if it does exist
            # check to see if password hash is equal to password hash in the database
            if check_password_hash(login_user['password'], request.form['pass']):
                # if password is correct then activate user session using the username
                session['username'] = request.form['username']
                return redirect(url_for('index')) # redirect to main route
            # if password does not match then...
            else: 
                # error takes in a string message
                error = 'Incorrect username/password'
                #return 'wrong password' # Login failed
        else:
            error = 'Incorrect username/password'
    # return login page and also pass in error message
    return render_template('login.html', error=error)

# Login
@app.route("/logout")
def logout():
    # remove the username from the session if logout button is pressed
    session.pop('username', None)
    # Flash a message to user to indicate they are logged out
    flash("You are now logged out")
    return redirect(url_for('index')) # redirect to main route

# Camera route
@app.route("/camera", methods = ['POST'])
def camera():
    print("Opening ASL Model!")
    try:
        direct = cwd + "/ASLClassifier.dat"
        print(direct)
        model=st.load(direct)
        print("SVM Loaded successfully..")
    except:
        model=st.trainSVM(17)
    
    #cap=cv2.VideoCapture(0)
    #cap=PiCamera(0)
    camera=PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    time.sleep(0.1)
    #rgbFrame = PiRGBArray(camera, size = camera.resolution)
    #frame1 = captureProcessFrame(camera, rgbFrame, 5)
    #frameCount = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    text= " "

    temp=0
    previouslabel=None # Past label
    previousText=" " # Past text
    label = None # current label
    
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): # Capture pi camera frames
        stream = frame.array # store frame input as array
        rawCapture.truncate(0) # take optional size
        img=stream # store stream as temp img
        cv2.rectangle(img, (300,300), (100,100), (0,255,0),0) # create rectangle one screen
        img1 = img[100:300, 100:300] # image stream ratio
        img_ycrcb = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB) # color format settings
        blur = cv2.GaussianBlur(img_ycrcb,(11,11),0) # Gaussian blur added to screen helps deal with frams quality and performance
        skin_ycrcb_min = np.array((0, 138, 67)) # color spaces min
        skin_ycrcb_max = np.array((255, 173, 133)) # color spaces max
        mask = cv2.inRange(blur, skin_ycrcb_min, skin_ycrcb_max)  # detecting the hand in the bounding box using skin detection
        imgres,contours,hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # track motion points
        cnt=ut.getMaxContour(contours,4000)	#store total motion points
        if cnt is not None: # is there something there?
            gesture,label=ut.getGestureImg(cnt,img1,mask,model)   # passing the trained model for prediction and fetching the result
            if(label!=None): # is the model finding something in the box that matches a label?
                if(temp==0): # if temp is 0
                    previouslabel=label # last label now label
                elif previouslabel==label: # still same gesture?
                    previouslabel=label # track again
                    temp+=1 # increse temp gesture count
                else: # otherwise
                    temp=0 # temp gesture back to 0
                if(temp==40): # has it been on screen for 40 temp counts?
                    if(label=='P'): # create sentence space if user does P
                        label=" " # lable space
                        text= text + label # add results to text
                    if(label=='Q'): # Wipe with Q(QUIT)
                        words = re.split(" +",text) # split result
                        words.pop() # push text off
                        text = " ".join(words) # fresh text
                        #text=previousText
                print(text) # print out your last gestures before quiting

            #cv2.imshow('PredictedGesture',gesture)				  # showing the best match or prediction
            cv2.putText(img,label,(50,150), font,8,(0,125,155),2)  # displaying the predicted letter on the main screen
            cv2.putText(img,text,(50,450), font,3,(0,0,255),2)
            
        cv2.imshow('Frame',img) # show on screen
        #cv2.imshow('Mask',mask)
        key = cv2.waitKey(1) & 0xFF # wait for q to quit
        if key == ord("q"): # is Q?
            #cap.release()        
            cv2.destroyAllWindows() # close OpenCV session
            camera.close()
            break # stop while

    return render_template("index.html")



# Camera route
@app.route("/camera2", methods = ['POST'])
def camera2():
    camera=PiCamera()
    camera.resolution = (320, 240)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(320, 240))
    time.sleep(0.1)
    print("Opening number dectector!")
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): # Capture pi camera frames
        stream = frame.array # store frame input as array
        rawCapture.truncate(0) # take optional size
        # read image
        img = stream

        # get hand data from the rectangle sub window on the screen
        cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
        crop_img = img[100:300, 100:300]

        # convert to grayscale
        grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

        # applying gaussian blur
        value = (35, 35)
        blurred = cv2.GaussianBlur(grey, value, 0)

        # thresholdin: Otsu's Binarization method
        _, thresh1 = cv2.threshold(blurred, 127, 255,
                                cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # show thresholded image
        cv2.imshow('Thresholded', thresh1)

        # check OpenCV version to avoid unpacking error
        (version, _, _) = cv2.__version__.split('.')

        if version == '3':
            image, contours, hierarchy = cv2.findContours(thresh1.copy(), \
                cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        elif version == '2':
            contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
                cv2.CHAIN_APPROX_NONE)

        # find contour with max area
        cnt = max(contours, key = lambda x: cv2.contourArea(x))

        # create bounding rectangle around the contour (can skip below two lines)
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(crop_img, (x, y), (x+w, y+h), (0, 0, 255), 0)

        # finding convex hull
        hull = cv2.convexHull(cnt)

        # drawing contours
        drawing = np.zeros(crop_img.shape,np.uint8)
        cv2.drawContours(drawing, [cnt], 0, (0, 255, 0), 0)
        cv2.drawContours(drawing, [hull], 0,(0, 0, 255), 0)

        # finding convex hull
        hull = cv2.convexHull(cnt, returnPoints=False)

        # finding convexity defects
        defects = cv2.convexityDefects(cnt, hull)
        count_defects = 0
        cv2.drawContours(thresh1, contours, -1, (0, 255, 0), 3)

        # applying Cosine Rule to find angle for all defects (between fingers)
        # with angle > 90 degrees and ignore defects
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]

            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])

            # find length of all sides of triangle
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)

            # apply cosine rule here
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57

            # ignore angles > 90 and highlight rest with red dots
            if angle <= 90:
                count_defects += 1
                cv2.circle(crop_img, far, 1, [0,0,255], -1)
            #dist = cv2.pointPolygonTest(cnt,far,True)

            # draw a line from start to end i.e. the convex points (finger tips)
            # (can skip this part)
            cv2.line(crop_img,start, end, [0,255,0], 2)
            #cv2.circle(crop_img,far,5,[0,0,255],-1)

        # define actions required
        if count_defects == 1:
            cv2.putText(img,"One", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 2:
            str = "Two"
            cv2.putText(img, str, (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        elif count_defects == 3:
            path = 'C:/Users/Iano/Desktop'
            cv2.imwrite(os.path.join(path , 'img.jpg'), img)
        elif count_defects == 4:
            cv2.putText(img,"4", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        else:
            cv2.putText(img,"Five", (50, 50),\
                        cv2.FONT_HERSHEY_SIMPLEX, 2, 2)

        # show appropriate images in windows
        cv2.imshow('Gesture', img)
        all_img = np.hstack((drawing, crop_img))
        cv2.imshow('Contours', all_img)

        k = cv2.waitKey(1) & 0xFF
        if k == ord("q"):
            cv2.destroyAllWindows() # close OpenCV session
            camera.close()
            return redirect(url_for("index"))
            break

@app.errorhandler(404) # error? tell user
def page_not_found(e):
    return """<html><body>
        Something went horribly wrong
        </body></html>""", 404
    
if __name__ == "__main__": # init app
    print("Running gesture based app...")
    # In order to use sessions you have to set a secret key for encryption purposes as a user could hack into the contents of a cookie and modify if there was no secret key used for signing the cookies.
    app.secret_key = 'mysecret' 
    app.run()
    
