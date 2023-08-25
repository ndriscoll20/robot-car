#! /usr/bin/python3

import RPi.GPIO as GPIO          
from time import sleep

# MotorA
in1 = 23
in2 = 24
ena = 25
temp1=1

# Right Motor
in3 = 27
in4 = 22
enb = 17

# Setup 
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT) # Left Motor 
GPIO.setup(in2,GPIO.OUT) # Left Motor
GPIO.setup(ena,GPIO.OUT) # Left Motor PWM
GPIO.setup(in3,GPIO.OUT) # Right Motor
GPIO.setup(in4,GPIO.OUT) # Right Motor
GPIO.setup(enb,GPIO.OUT) # Right Motor PWM
# Initialize 0 speed
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
pL=GPIO.PWM(ena,1000)
pR=GPIO.PWM(enb,1000)
pL.start(35)
speed = 35
pR.start(speed)

while(True):

    x = input()

    if x == 'r':
        print('run')
        if temp1==1:
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            print("forward")
            x='z'
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            print("backward")
            x='z'

    elif x == 's':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.low)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='u':
        speed = speed+1
        print(speed)
        pR.ChangeDutyCycle(speed)
        x='z'

    elif x=='d':
        speed = speed-1
        print(speed)
        pR.ChangeDutyCycle(speed)
        x='z'

    elif x=='e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
