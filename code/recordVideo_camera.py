#!/usr/bin/env

from picamera import PiCamera
from time import sleep

# initializing camera object
camera = PiCamera()

# camera rotaion
camera.rotation = 180

# camera transparency
alpha_level = 200 # from 0 to 255

# start recording video
i = 1
camera.start_recording('~/Documents/rmelo19-raspberrypi/VIDEO/video%s.h264', % i)

# do nothing for 10s.
sleep(10)

# stop recording video
camera.stop_recording()

# close preview
camera.stop_preview()

# to play the video
# omxplayer video0.h264