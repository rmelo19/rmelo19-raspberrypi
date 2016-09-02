#!/usr/bin/env

from picamera import PiCamera
from time import sleep

# initializing camera object
camera = PiCamera()

# camera rotaion
camera.rotation = 180

# camera transparency
alpha_level = 200 # from 0 to 255

# open preview
camera.start_preview(alpha=200)

# do nothing for 10s
sleep(10)

# close preview
camera.stop_preview()