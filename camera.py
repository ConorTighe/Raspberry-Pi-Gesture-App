import picamera # picamera library is used as a python interface to the raspberry pi camera.

"""
    Simple python script that imports picamera library in order to use the raspberry camera
    and program it to take a picture when this script is executed.

    Ref: https://www.raspberrypi.org/documentation/usage/camera/python/README.md
"""

# Setup the camera up in a way that it closes when the program is done.
print("Taking a picture!")
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720) # Configuring the resolution of the camera when a picture is taken.
    camera.capture("/home/pi/Desktop/camera/newimage.jpg") # save the picture to this address
print("Picture taken..")
