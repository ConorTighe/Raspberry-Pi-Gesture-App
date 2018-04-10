# Gesture Based UI - Raspberry Pi and OpenCV
#### *Gesture Based UI Development - Lecturer: Damien Costello - 4th Year (Hons) Software Development, GMIT*
This repository contains a project for 4th Year module Gesture Based UI Development, developed by [Conor Tighe](https://github.com/ConorTighe1995) and [Ian Burke](https://github.com/ianburkeixiv). The project is a gesture based sign language Web App using [Flask](http://flask.pocoo.org/) as the server, a [Raspberry Pi 3 Model B](https://www.raspberrypi.org/) and [PiCamera module](https://www.raspberrypi.org/documentation/usage/camera/README.md), and [OpenCV](https://opencv.org/) for gesture recognition.

**_Click [here](https://github.com/ConorTighe1995/Raspberry-Pi-Gesture-App/raw/master/Installation%20and%20Configuration%20Guide.docx) for the Raspberry Pi installation and configuration Guide_**

**_Click [here](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) for tutorial on installing OpenCV on the Raspberry Pi_**


## How to run
1. Download the [zip](https://github.com/ConorTighe1995/Raspberry-Pi-Gesture-App/archive/master.zip)
2. Extract/Unzip the repository
3. Open a command terminal.
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

## Purpose of the application
The application will allow users to practice [Sign Language](https://en.wikipedia.org/wiki/Sign_language) by printing out a letter based on their hand gesture. When the Web Application is running, a user can press a button to turn on the Raspberry Pi Camera Module where a window opens up displaying the live video stream. A rectangle box is displayed on the screen where users place their hand in to make gestures. The program reads these gestures and returns a printed letter to the screen based on a certain hand gesture.


### Machine learning
#### How does the app recognise the gestures?
Supervised machine learning algorithms can apply what has been learned in the past to new data using labeled examples to predict future events. Starting from the analysis of a known training dataset, the learning algorithm produces an inferred function to make predictions about the output values. The system is able to provide targets for any new input after sufficient training. The learning algorithm can also compare its output with the correct, intended output and find errors in order to modify the model accordingly.

#### What is the SVM Model that performs the gesture recognition?
A [Support Vector Machine (SVM)](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html) is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples.

#### SVM accuracy:
The [SVM](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html) model is a basic but effective way of identifying objects using supervised machine learning with images, but the results can vary, to maxmize your experience of the app we recomemend having a plane background and keeping moving objects away from the hitbox. In the right circumstances this app can be used as a great tool for beginers looking to expand there knollege of communicating with sign langauge without needing a teacher or another person to practice with.

## Gestures identified as appropiate for this application
(static/assets/ASL.jpg "Gesturefile")
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



## Conclusion & Recommendations
In this project, we have taken a raspberry pi and used it to run our gesture based flask web app. We have learned and gained a lot working with a Raspberry Pi and OpenCV. It was something different and challanging. It was interesting to work on the gesture recognition and to dive into machine learning. We did encounter some problems along the way but with help from stack overflow and other forums, we managed our way through to a working application. Majoity of the problems were related to the installation of openCV on the Raspberry Pi. Since the Raspberry Pi is such a small and lightweight computer and OpenCV is a vast and heavy use library, it wasn't an easy process. Following the OpenCV [tutorial](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/) mentioned above, we had to change around with the settings on the Pi and be patient with the compile process. After successfully installating OpenCV, we were able to run our gesture app on the Raspberry Pi using the Pi Camera Module. 

# Refrences
- [Raspberry Pi](https://www.raspberrypi.org/)
- [OpenCV](https://opencv.org/about.html)
- [Supervised machine learning](http://www.expertsystem.com/machine-learning-definition/)
- [SVM](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html)
