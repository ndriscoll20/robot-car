#! /usr/bin/env python3

#Raspberry Pi
import RPi.GPIO as GPIO

class Motor:
    '''A PWM DC motor driven by three pins on a Raspberry Pi.'''

    def __init__ (self, pinFwd, pinBack, pinPwm, frequency=100, maxSpeed=100):
        #  Configure GPIO
        GPIO.setmode (GPIO.BCM)
        GPIO.setwarnings (False)

        GPIO.setup(pinFwd,  GPIO.OUT)
        GPIO.setup(pinBack, GPIO.OUT)
        GPIO.setup(pinPwm, GPIO.OUT)

        #  get a handle to PWM
        self._frequency = frequency
        self._maxSpeed = maxSpeed
        self._Fwd  = pinFwd
        self._Back = pinBack
        self._pwm = GPIO.PWM(pinPwm, frequency)
        self.stop()

    def forward (self, speed = None):
        '''Spin the motor forward'''
        if speed == None:
            speed = self._maxSpeed
        self.run (speed)

    def reverse (self, speed = None):
        '''Spin the motor in reverse'''
        if speed == None:
            speed = -self._maxSpeed
        self.run (-1 * speed)

    def stop (self):
        '''Stop the motor'''
        self.run (0)

    def run (self, speed=None):
        '''Start the motor. If no speed is given, starts moving
        forward at the max speed.'''
        
        #  set limits
        if speed == None:
            speed = self._maxSpeed
        speed = min (self._maxSpeed, speed)
        speed = max (-self._maxSpeed, speed)

        #  turn on the motors
        if speed < 0:
            GPIO.output(self._Fwd, 0)
            GPIO.output(self._Back, 1)
            self._pwm.start(-1.0*speed)
        else:
            GPIO.output(self._Fwd, 1)
            GPIO.output(self._Back, 0)
            self._pwm.start(speed)
