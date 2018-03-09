import picamera # picamera library is used as a python interface to the raspberry pi camera.
from time import sleep 
from subprocess import call #subprocess is a library for python to interact with command terminal

"""
    Simple python script that imports picamera library in order to use the raspberry camera
    and program it to take a video when this script is executed.

    Ref: https://www.raspberrypi.org/documentation/usage/camera/python/README.md
"""
# Setup the camera up in a way that it closes when the program is done.
print("Recording..")
with picamera.PiCamera() as camera:
    camera.start_recording("video.h264") # Start recording and save the film to this address in h264 format
    sleep(5) # sleep 5 seconds and suspend further operations, in other words, record for only 5 seconds and then stop as shown below
    camera.stop_recording() # stop the recording
    print("Recording ended")
    
# In order to convert the video from h264 to mp4, we need to install gpac module on the raspberry pi
# In the command terminal, enter: sudo apt-get install gpac
# Once installed, we can use a command to convert file formats
# Instead of opening up the command terminal and converting the video to mp4 after every video recorded..
# we can include the command in this script.
# Ref: http://raspi.tv/2013/another-way-to-convert-raspberry-pi-camera-h264-output-to-mp4
# Ref: https://gpac.wp.imt.fr/home/

# Define the command to convert the recoreded video from h264 format to mp4 format
print("Converting video format to mp4..")
command = "MP4Box -add video.h264 convertedVideo.mp4"

# Execute the command
call([command], shell=True) #Open command terminal and execute command.
print("Video converted to mp4")
