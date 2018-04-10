# Gesture Based UI - Raspberry Pi and OpenCV
#### *Gesture Based UI Development - Lecturer: Damien Costello - 4th Year (Hons) Software Development, GMIT*
This repository contains a project for 4th Year module Gesture Based UI Development, developed by [Conor Tighe](https://github.com/ConorTighe1995) and [Ian Burke](https://github.com/ianburkeixiv). The project is a gesture based sign language Web App using [Flask](http://flask.pocoo.org/) as the server, a [Raspberry Pi 3](https://www.raspberrypi.org/) and [PiCamera module](https://www.raspberrypi.org/documentation/usage/camera/README.md), and [OpenCV](https://opencv.org/) for gesture recognition.

## Purpose of the application
The application will allow users to practice [Sign Language](https://en.wikipedia.org/wiki/Sign_language) by printing out a letter based on their hand gesture. When the Web Application is running, a user can press a button to turn on the Raspberry Pi Camera Module where a window opens up displaying the live video stream. A rectangle box is displayed on the screen where users place their hand in to make gestures. The program reads these gestures and returns a printed letter to the screen based on a certain hand gesture.

### User guide
This project is hosted by Flask, in order to run the app you must do the following:

1. Open the command line

2. Navigate to the project location on your operating system

3. enter 'SET FLASK_APP=app.py' into the console.

4. enter 'flask run'

You should then be asked to navigate to 'http://127.0.0.1:5000/' in your browser. From here you can choose the ASL(American Sign Language) option or the sign langauge number convertor. If you choose 
the ASL option the classifier should load, if the classifier cannot be found then the application will attempt to start training images for recognision. If this happens make sure the TrainData file is unzipped 
and the location is avalible on your machine or you will see errors appear asking for these images.

#### The app is running! now how do I actually use it?
Don't hold your hand in the hitbox while change signs as this confuses the model and creates randonm results, we recommend making the sign outside the box and then moving it in for detections. press Q on the keyboard to quit the detection window.

## Machine learning
### How does the app recognise the gestures?
Supervised machine learning algorithms can apply what has been learned in the past to new data using labeled examples to predict future events. Starting from the analysis of a known training dataset, the learning algorithm produces an inferred function to make predictions about the output values. The system is able to provide targets for any new input after sufficient training. The learning algorithm can also compare its output with the correct, intended output and find errors in order to modify the model accordingly.

### What is the SVM Model that performs the gesture recognition?
A Support Vector Machine (SVM) is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples.

#### SVM accuracy:
The SVM model is a basic but effective way of identifying objects using supervised machine learning with images, but the results can vary, to maxmize your experience of the app we recomemend having a plane background and keeping moving objects away from the hitbox. In the right circumstances this app can be used as a great tool for beginers looking to expand there knollege of communicating with sign langauge without needing a teacher or another person to practice with.

## Gestures identified as appropiate for this application

## Hardware used in creating the application
A [Raspberry Pi](https://www.raspberrypi.org/) is a credit card-sized computer originally designed for education, inspired by the 1981 BBC Micro. Creator Eben Upton's goal was to create a low-cost device that would improve programming skills and hardware understanding at the pre-university level. But thanks to its small size and accessible price, it was quickly adopted by students and electronics enthusiasts for projects that require more than a basic microcontroller (such as Arduino devices). It is slower than a modern laptop or desktop computer but is still a complete Linux computer and can provide all the expected abilities that implies, at a low-power consumption level.

The Raspberry Pi is open hardware, with the exception of the primary chip on the Raspberry Pi, the [Broadcomm SoC](https://www.raspberrypi.org/documentation/hardware/raspberrypi/bcm2837/README.md) (System on a Chip), which runs many of the main components of the board–CPU, graphics, memory, the USB controller, etc. 

The Raspberry Pi model used for this project is a [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) which is the third generation Raspberry Pi. This model has a Quad-Core 64bit CPU, 1GB RAM, 4 x USB ports, 4 pole Stereo output and Composite video port, HDMI, Ethernet port, CSI Camera port, DSI display port, Micro SD port,  Wifi and Bluetooth.

## Architecture for the solution

## Conclusion & Recommendations

# Refrences
- [Supervised machine learning](http://www.expertsystem.com/machine-learning-definition/)
- [SVM](https://docs.opencv.org/2.4/doc/tutorials/ml/introduction_to_svm/introduction_to_svm.html)