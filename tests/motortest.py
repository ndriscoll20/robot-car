#! /usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)

class Motor:
    def __init__ (self, pinFwd, pinBack, pinPwm, frequency=100, maxSpeed=100):
        #  Configure GPIO
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

    def forward (self, speed):
        self._move (speed)

    def backwards (self, speed):
        self._move (-speed)

    def stop (self):
        self._move (0)

    def _move (self, speed):
        #  set limits
        if speed > self._maxSpeed:
            speed = self._maxSpeed
        if speed < -self._maxSpeed:
            speed = -self._maxSpeed

        #  turn on the motors
        if speed < 0:
            GPIO.output(self._Fwd, 0)
            GPIO.output(self._Back, 1)
            self._pwm.start(-speed)
        else:
            GPIO.output(self._Fwd, 1)
            GPIO.output(self._Back, 0)
            self._pwm.start(speed)

class Wheelie:
    def __init__ (self):
        self.rightWheel = Motor(27, 22, 17)
        self.leftWheel = Motor(23, 24, 25)

    def stop (self):
        self.leftWheel.stop()
        self.rightWheel.stop()

    def goForward (self, speed = 100):
        self.rightWheel.forward (speed)
        self.leftWheel.forward (speed)

    def goBackward (self, speed = 100):
        self.rightWheel.backwards (speed)
        self.leftWheel.backwards (speed)

    def goLeft (self, speed = 100):
        self.rightWheel.forward (speed)
        self.leftWheel.backwards (speed)

    def goRight (self, speed = 100):
        self.rightWheel.backwards (speed)
        self.leftWheel.forward (speed)

def main():
    wheelie = Wheelie()
    wheelie.goForward()
    time.sleep(2)
    wheelie.goLeft()
    time.sleep(2)
    wheelie.goBackward(50)
    time.sleep(2)
    wheelie.goRight()
    time.sleep(2)
    wheelie.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()

