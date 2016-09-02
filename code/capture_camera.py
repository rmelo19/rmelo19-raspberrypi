#!/usr/bin/env

from picamera import PiCamera
from time import sleep

# initializing camera object
camera = PiCamera()

# camera rotaion
camera.rotation = 180
# resolution
camera.resolution = (2592, 1944) # max resolution
# frame rate
camera.framerate = 15 # reduce frame rate to achieve max resolution
# add annotation to picture
camera.annotate_text = "Hello world!"
camera.annotate_text_sizef = 50 # from 6 to 160 (32 is the default)
from picamera import Color
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('blue')

# image effects
# none, negative, solarize, sketch, denoise, emboss, oilpaint, hatch
# gpen, pastel, watercolor, film, blur, saturation, colorswap, washedout,
# posterise, colorpoint, colorbalance, cartoon, deinterlace1, and deinterlace2
camera.image_effect('colorswap') # default is none

# auto white balance
# off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, and horizon
# list at camera.AWB_MODES
camera.awb_mode = 'sunlight' # default is none

# exposure mode
# off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, and fireworks
# list at camera.EXPOSURE_MODES.
camera.exposure_mode = 'night' # default is auto

# brightness
camera.brightness = 70 # from 0 to 100 (50 is the default)
# contrast
camera.contrast = 70 # from 0 to 100 (50 is the default)

# camera transparency
alpha_level = 200 # from 0 to 255

# open preview
camera.start_preview(alpha=200)

# do nothing for 2s. Let light come!
sleep(2)

# take the picture
i = 0;
camera.capture('/home/rmelo19-raspberrypi/IMG/image%s.jpg', % i)

# close preview
camera.stop_preview()
