# Gesture Based UI - Raspberry Pi and OpenCV
#### *Gesture Based UI Development - Lecturer: Damien Costello - 4th Year (Hons) Software Development, GMIT*
This repository contains a project for 4th Year module Gesture Based UI Development, developed by [Conor Tighe](https://github.com/ConorTighe1995) and [Ian Burke](https://github.com/ianburkeixiv). The project is a gesture based sign language Web App using [Flask](http://flask.pocoo.org/) as the server, a [Raspberry Pi 3 Model B](https://www.raspberrypi.org/) and [PiCamera module](https://www.raspberrypi.org/documentation/usage/camera/README.md), and [OpenCV](https://opencv.org/) for gesture recognition.

<p align="center"> 
<img src="https://user-images.githubusercontent.com/22341150/39208148-07ab5fa8-47fa-11e8-8799-88fe0af5432d.PNG">
</p>

**_Click [here](https://github.com/ConorTighe1995/Raspberry-Pi-Gesture-App/raw/master/Installation%20and%20Configuration%20Guide.docx) for the Raspberry Pi installation and configuration Guide_**

**_Click [here](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) for tutorial on installing OpenCV on the Raspberry Pi_**

### Video Demo 
https://youtu.be/zZEcTDbVVc0

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/zZEcTDbVVc0/0.jpg)](https://youtu.be/zZEcTDbVVc0)


## How to run
1. Download the [zip](https://github.com/ConorTighe1995/Raspberry-Pi-Gesture-App/archive/master.zip)
2. Extract/Unzip the repository
3. Using a Raspberry Pi, Open a command terminal.
4. To run the application, we need to run a python virtual environment. A virtual environment is a special tool used to keep the dependencies required by different projects in separate places by creating isolated, independent Python environments for each of them. To run the virtual environment, enter the following:
```bash
pi@raspberrypi:~ $ source ~/.profile

pi@raspberrypi:~ $ workon cv
```
5. Once in the virtual environment (cv), go to the the directory where the repository is located. For example:
```bash
(cv) pi@raspberrypi:~ $ cd Desktop
(cv) pi@raspberrypi:/Desktop $ cd Raspberry-Pi-Gesture-App
```
6. Run the application:
```bash
(cv) pi@raspberrypi:/Desktop/Raspberry-Pi-Gesture-App $ python app.y
```

You should then be asked to navigate to 'http://127.0.0.1:5000/' in your browser. From here you can choose the ASL(American Sign Language) option or the sign langauge number convertor. If you choose 
the ASL option the classifier should load, if the classifier cannot be found then the application will attempt to start training images for recognision. If this happens make sure the TrainData file is unzipped 
and the location is avalible on your machine or you will see errors appear asking for these images.

#### The app is running! Now how do I actually use it?
Don't hold your hand in the hitbox while change signs as this confuses the model and creates randonm results, we recommend making the sign outside the box and then moving it in for detections. Press Q on the keyboard to quit the detection window.

#### User Guide
![](https://user-images.githubusercontent.com/22341150/39207167-2ec1439e-47f7-11e8-9bcd-a94138763449.gif)

#### Report an Issue
![](https://user-images.githubusercontent.com/22341150/39207168-2ee94150-47f7-11e8-9311-4a32405647c1.gif)

### Some sign gestures
![](https://user-images.githubusercontent.com/22341150/39207569-3308e366-47f8-11e8-9c9c-81453041d3f4.png)

![](https://user-images.githubusercontent.com/22341150/39207570-332acb2a-47f8-11e8-9527-cab3fda36b26.png)

![](https://user-images.githubusercontent.com/22341150/39207572-3348bd42-47f8-11e8-9455-20700d62d9e7.png)

## Purpose of the application
The application will allow users to practice [Sign Language](https://en.wikipedia.org/wiki/Sign_language) by printing out a letter based on their hand gesture. When the Web Application is running, a user can press a button to turn on the Raspberry Pi Camera Module where a window opens up displaying the live video stream. A rectangle box is displayed on the screen where users place their hand in to make gestures. The program reads these gestures and returns a printed letter to the screen based on a certain hand gesture.


### Machine learning
#### How does the app recognise the gestures?
Supervised machine learning algorithms can apply what has been learned in the past to new data using labeled examples to predict future events. Starting from the analysis of a known training dataset, the learning algorithm produces an inferred function to make predictions about the output values. The system is able to provide targets for any new input after sufficient training. The learning algorithm can also compare its output with the correct, intended output and find errors in order to modify the model accordingly.

#### What is the SVM Model that performs the gesture recognition?
A [Support Vector Machine (SVM)](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html) is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples.

#### SVM accuracy:
The [SVM](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html) model is a basic but effective way of identifying objects using supervised machine learning with images, but the results can vary, to maxmize your experience of the app we recomemend having a plane background and keeping moving objects away from the hitbox. In the right circumstances this app can be used as a great tool for beginers looking to expand there knollege of communicating with sign langauge without needing a teacher or another person to practice with.

### User Authentication
#### Session
To implement a user login and registration service to the web app, a session is needed to allow you to store information specific to a user from one request to the next. It keeps track of the active user until the user logs out. Session allows us to restrict users from certain features such as the gesture recognition. If a person is not registered on the web app then they are restricted from the features. Sessions is implemented on top of cookies and signs the cookies cryptographically.

![](https://user-images.githubusercontent.com/22341150/39085860-04aa195a-4581-11e8-904e-768da53181cc.PNG)

#### Message Flashing
Flashing messages was introduced to let users know if they are signed in or logged out. Good applications and user interfaces are all about feedback. The flashing system basically makes it possible to record a message at the end of a request and access it on the next request. By using the Jinja template engine that’s included in Flask, we were able to display a message across the page when the user signs in or logs out.

![](https://user-images.githubusercontent.com/22341150/39085836-8f494bc2-4580-11e8-89c8-d85706838c9d.PNG)

![](https://user-images.githubusercontent.com/22341150/39085784-e267359a-457f-11e8-9913-5c6735c7daca.PNG)


#### Password Hashing
When you have user accounts and you give them passwords to those accounts, it is very important that the passwords are not stored in the database unhashed. However, just hashing the passwords is barely more secure because of Rainbow table attacks. A rainbow table attack is a type of hacking where the attacker uses a rainbow hash table to crack the passwords stored in a database system. The attacker will take a dictionary of words or a list of common passwords and hashes those words using a specific function (md5 or SHA) which are organised then in a list and compare that list with the hashes in a database with the objective to find a matching hash.  To counter this, a salt is added to the hashed passwords. A salt is random generated data that is used as an additional input to a one-way function that hashes passwords. Salts are used to defend against dictionary attacks or rainbow table attacks. Werkzeug provides a security utility helper to add a salt and generate hashed passwords in flask. Werkzeug is a WSGI (Web Server Gateway Interface) utility library for Python. For example:
```Python
from werkzeug.security import generate_password_hash, check_password_hash 
generate_password_hash(password, method='pbkdf2:sha256', salt_length=8) 
```
This helper uses a one-way function to create a hash that is not reversible from the passed in plain text password. The method sets the hashing algorithm to use and the salt_length sets the length of the salt in letters. 
```Python
check_password_hash(pwhash, password)
```
The check_password_hash() checks that the hashed password passed in is equal to the hashed password in the database.

#### MongoDB Cloud
[mLab](https://mlab.com/) is a fully managed cloud database service that hosts MongoDB databases. mLab runs on cloud providers Amazon, Google, and Microsoft Azure, and has partnered with platform-as-a-service providers. Usernames and hashed passwords are stored in the database.

![](https://user-images.githubusercontent.com/22341150/39085786-e2b97274-457f-11e8-96b1-af26d77d4cf6.PNG)

## Gestures identified as appropiate for this application
![Gestures](static/assets/ASL.jpg "Gesturefile")
## Hardware used in creating the application
#### Raspberry Pi 3 Model B
A [Raspberry Pi](https://www.raspberrypi.org/) is a credit card-sized computer originally designed for education, inspired by the 1981 BBC Micro. Creator Eben Upton's goal was to create a low-cost device that would improve programming skills and hardware understanding at the pre-university level. But thanks to its small size and accessible price, it was quickly adopted by students and electronics enthusiasts for projects that require more than a basic microcontroller (such as Arduino devices). It is slower than a modern laptop or desktop computer but is still a complete Linux computer and can provide all the expected abilities that implies, at a low-power consumption level.

The Raspberry Pi is open hardware, with the exception of the primary chip on the Raspberry Pi, the [Broadcomm SoC](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2837/README.md) (System on a Chip), which runs many of the main components of the board–CPU, graphics, memory, the USB controller, etc. 

The Raspberry Pi model used for this project is a [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) which is the third generation Raspberry Pi. This model has a Quad-Core 64bit CPU, 1GB RAM, 4 x USB ports, 4 pole Stereo output and Composite video port, HDMI, Ethernet port, CSI Camera port, DSI display port, Micro SD port,  Wifi and Bluetooth.
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/22341150/38555690-f7a5ee84-3cbe-11e8-9622-2c7700dcbfc5.jpg">
</p>

#### Camera Module V2
The v2 Camera Module has a Sony IMX219 8-megapixel sensor. It supports 1080p30, 720p60 and VGA90 video modes, as well as still capture. The camera works with all models of Raspberry Pi 1, 2, and 3. It can be accessed through the MMAL and V4L APIs, and there are numerous third-party libraries built for it, including the Picamera Python library which is used in this project. It attaches via a 15cm ribbon cable to the CSI port on the Raspberry Pi.
<p align="center">
  <img src="https://user-images.githubusercontent.com/22341150/38555697-01d20460-3cbf-11e8-9c04-625d9effda03.jpg">
</p>

## Architecture for the solution
#### Python
The main programming language used in this project is [Python.](https://www.python.org/)

#### Flask
[Flask](http://flask.pocoo.org/) is a Python micro web framework that provides tools, libraries and technologies that allow us to build a web application. 

#### OpenCv
[OpenCV (Open Source Computer Vision Library)](https://opencv.org/) is an open source computer vision and machine learning software library. OpenCV was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.

The library has more than 2500 optimized algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect and recognize faces, identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, stitch images together to produce a high resolution image of an entire scene, find similar images from an image database, remove red eyes from images taken using flash, follow eye movements, recognize scenery and establish markers to overlay it with augmented reality, etc. OpenCV has more than 47 thousand people of user community and estimated number of downloads exceeding 14 million. The library is used extensively in companies, research groups and by governmental bodies.

It has C++, Python, Java and MATLAB interfaces and supports Windows, Linux, Android and Mac OS.

#### MongoDB
MongoDB is one of the most popular open source NoSQL database that uses a document-oriented data model. It stores data in JSON (JavaScript Object Notation) like documents. It is non-relational database with dynamic schema. MongoDB is horizontally scalable and easy for both the developers and administrators to manage. MongoDB is written in C++ and is currently being used by some big companies like Google, Facebook, Cisco, Ebay and SAP.

In this project, we use MongoDB to store usernames and hashed passwords as past of our user authentication process.

## Conclusion & Recommendations
In this project, we have taken a raspberry pi and used it to run our gesture based flask web app. We have learned and gained a lot working with a Raspberry Pi and OpenCV. It was something different and challanging. It was interesting to work on the gesture recognition and to dive into machine learning. We did encounter some problems along the way but with help from stack overflow and other forums, we managed our way through to a working application. Majoity of the problems were related to the installation of openCV on the Raspberry Pi. Since the Raspberry Pi is such a small and lightweight computer and OpenCV is a vast and heavy use library, it wasn't an easy process. Following the OpenCV [tutorial](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) mentioned above, we had to change around with the settings on the Pi and be patient with the compile process. The next few problems encountered after that was to do with the merging of OpenCV and the Pi Camera. OpenCV is mostly used with usb cameras and laptop web cams and therefore we had to adjust the code around in order for it to work with the Pi Camera module. After that the application ran successfully. It took a lot of work and time but in the end, it was very rewarding to get everything working.

# Refrences
- [Raspberry Pi](https://www.raspberrypi.org/)
- [OpenCV](https://opencv.org/about.html)
- [Supervised machine learning](http://www.expertsystem.com/machine-learning-definition/)
- [SVM](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html)
