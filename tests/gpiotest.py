#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

#  set GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#  set GPIO pin mode
GPIO.setup(24, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

#  set speed of pwm
pL=GPIO.PWM(25, 1000)
pR=GPIO.PWM(17, 1000)
pL.start(40)
pR.start(40)

#  turn motors off
GPIO.output(7,0)
GPIO.output(8,0)
GPIO.output(9,0)
GPIO.output(10,0)

#  turn right motor forward
GPIO.output(7,0)
GPIO.output(8,1)

#  turn left motor forward
GPIO.output(9,0)
GPIO.output(10,1)

time.sleep(1)

#  Reset GPIO and turn off motors
GPIO.cleanup()

