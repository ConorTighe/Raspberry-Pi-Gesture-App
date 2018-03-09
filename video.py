import picamera # picamera library is used as a python interface to the raspberry pi camera.
from time import sleep 

"""
    Simple python script that imports picamera library in order to use the raspberry camera
    and program it to take a picture when this script is executed.

    Ref: https://www.raspberrypi.org/documentation/usage/camera/python/README.md
"""
# Setup the camera up in a way that it closes when the program is done.
print("Video started..")
with picamera.PiCamera() as camera:
    camera.start_recording("/home/pi/Desktop/camera/video.h264") # Start recording and save the film to this address in h264 format
    sleep(5) # sleep 5 seconds and suspend further operations, in other words, record for only 5 seconds and then stop as shown below
    camera.stop_recording() # stop the recording
    print("Video done")
    
    
