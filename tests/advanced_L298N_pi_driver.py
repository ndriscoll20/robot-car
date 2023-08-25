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
GPIO.setup(in1, GPIO.OUT) # Left Motor 
GPIO.setup(in2, GPIO.OUT) # Left Motor 
GPIO.setup(ena, GPIO.OUT) # Left Motor 
GPIO.setup(in3, GPIO.OUT) # Right Motor
GPIO.setup(in4, GPIO.OUT) # Right Motor
GPIO.setup(enb, GPIO.OUT) # Right Motor

# Initialize 0 speed
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
pL=GPIO.PWM(ena,1000)
pR=GPIO.PWM(enb,1000)
#Lowest Starting Speed:
lSpeed = 33
rSpeed = 36
pL.start(lSpeed)
pR.start(rSpeed)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("Controls: ")
print("Directions: r-run s-stop f-forward b-backward")
print("Speed:      l-low m-medium h-high")
print("Exit:       e-exit")
print("\n")    

def increase_forward(lSpeed,rSpeed):
    if lSpeed >= 0 or rSpeed >=0:
        lSpeed = lSpeed + 2
        rSpeed = rSpeed + 2
    else:
        lSpeed = lSpeed - 2
        rSpeed = rSpeed - 2
    pL.ChangeDutyCycle(lSpeed)
    pR.ChangeDutyCycle(rSpeed)
    return lSpeed,rSpeed

def increase_backward(lSpeed,rSpeed):
    if lSpeed <= 0 or rSpeed <= 0:
        lSpeed = lSpeed - 2
        rSpeed = rSpeed - 2
    else:
        lSpeed = lSpeed + 2
        rSpeed = rSpeed + 2
    pL.ChangeDutyCycle(lSpeed)
    pR.ChangeDutyCycle(rSpeed)
    return lSpeed,rSpeed

def turn_left(lSpeed,rSpeed):
    lSpeed = lSpeed - 1
    rSpeed = rSpeed + 2
    pL.ChangeDutyCycle(lSpeed)
    pR.ChangeDutyCycle(rSpeed)
    return lSpeed,rSpeed

def turn_right(lSpeed,rSpeed):
    lSpeed = lSpeed + 2
    rSpeed = rSpeed - 1
    pL.ChangeDutyCycle(lSpeed)
    pR.ChangeDutyCycle(rSpeed)
    return lSpeed,rSpeed

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
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


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        pL.ChangeDutyCycle(35)
        pR.ChangeDutyCycle(35)
        x='z'

    elif x=='m':
        print("medium")
        pL.ChangeDutyCycle(50)
        pR.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        pL.ChangeDutyCycle(80)
        pR.ChangeDutyCycle(80)
        x='z'
    
    elif x=='i':
        print('increase speed')
        lSpeed,rSpeed = increase_forward(lSpeed,rSpeed)
    elif x=='k':
        print('decrease speed')
        lSpeed,rSpeed = increase_backward(lSpeed,rSpeed)
    elif x=='j':
        print('turn left')
        lSpeed,rSpeed = turn_left(lSpeed,rSpeed)
    elif x=='l':
        print('turn right')
        lSpeed,rSpeed = turn_right(lSpeed,rSpeed)
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
