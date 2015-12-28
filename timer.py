#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Mode assignments
ON = GPIO.LOW
OFF = GPIO.HIGH

# LED assignment
RedPin = 11
GreenPin = 12

# Timer setting in minutes, adjust to your needs
# Here time is set for eight minutes
seconds = 60 * 8

# GPIO settings
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RedPin, GPIO.OUT)
GPIO.output(RedPin, OFF)
GPIO.setup(GreenPin, GPIO.OUT)
GPIO.output(GreenPin, OFF)

try:
    while True:
        print 'The oven is hot, baking...'
        GPIO.output(RedPin, ON)
        GPIO.output(GreenPin, OFF)

        time.sleep(seconds)

        print 'Stuff is ready!'
        GPIO.output(RedPin, OFF)
        GPIO.output(GreenPin, ON)

        while True:
            print "Take the stuff out of the oven!"
            time.sleep(10)

# When Ctrl+C is pressed...
except KeyboardInterrupt:
    GPIO.output(RedPin, OFF)
    GPIO.output(GreenPin, OFF)
    GPIO.cleanup()

