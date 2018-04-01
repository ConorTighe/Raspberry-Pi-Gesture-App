import argparse
import json
from flask import Flask, render_template, request, jsonify
import requests
import cv2
import numpy as np
import math
import os
import numpy as np
import util as ut
import svm_train as st 
import re


cap = cv2.VideoCapture(0)
app = Flask(__name__)

# For setting the flags for app
FLAGS = None

# Get the current directory
cwd = os.getcwd();

# Home route
@app.route("/")
def index():
    print("serving index...")
    return render_template("index.html")

# Camera route
@app.route("/camera", methods = ['POST'])
def camera():
    model=st.trainSVM(17)
    cap=cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text= " "

    temp=0
    previouslabel=None
    previousText=" "
    label = None
    while(cap.isOpened()):
        _,img=cap.read()
        cv2.rectangle(img, (300,300), (100,100), (0,255,0),0)
        img1 = img[100:300, 100:300]
        img_ycrcb = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
        blur = cv2.GaussianBlur(img_ycrcb,(11,11),0)
        skin_ycrcb_min = np.array((0, 138, 67))
        skin_ycrcb_max = np.array((255, 173, 133))
        mask = cv2.inRange(blur, skin_ycrcb_min, skin_ycrcb_max)  # detecting the hand in the bounding box using skin detection
        imgres,contours,hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnt=ut.getMaxContour(contours,4000)			
        if cnt is not None:
            gesture,label=ut.getGestureImg(cnt,img1,mask,model)   # passing the trained model for prediction and fetching the result
            if(label!=None):
                if(temp==0):
                    previouslabel=label
                elif previouslabel==label:
                    previouslabel=label
                    temp+=1
                else:
                    temp=0
                if(temp==40):
                    if(label=='P'):
                        label=" "
                        text= text + label
                    if(label=='Q'):
                        words = re.split(" +",text)
                        words.pop()
                        text = " ".join(words)
                        #text=previousText
                print(text)

            #cv2.imshow('PredictedGesture',gesture)				  # showing the best match or prediction
            cv2.putText(img,label,(50,150), font,8,(0,125,155),2)  # displaying the predicted letter on the main screen
            cv2.putText(img,text,(50,450), font,3,(0,0,255),2)
            
        cv2.imshow('Frame',img)
        #cv2.imshow('Mask',mask)
        k = 0xFF & cv2.waitKey(10)
        if k == 27:
            break


cap.release()        
cv2.destroyAllWindows()


@app.errorhandler(404)
def page_not_found(e):
    return """<html><body>
        Something went horribly wrong
        </body></html>""", 404
    
def main(_):
    print("Running gesture based app...")
    app.run()
    