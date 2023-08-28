#! /usr/bin/python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
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
        self.move (speed)

    def backwards (self, speed):
       self.move (-speed)

    def stop (self):
        self.move (0)

    def move (self, speed):
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
        self.rightWheel = Motor (27, 22, 17)
        self.leftWheel = Motor (23, 24, 25)

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
        self.rightWheel.backwards (speed)
        self.leftWheel.forward (speed)

    def goRight (self, speed = 100):
        self.rightWheel.forward (speed)
        self.leftWheel.backwards (speed)

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'move',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.wheelie = Wheelie()
        print('Wheelie Class Started')

    def listener_callback(self, msg):
        print('Received Message', msg.data)
        command = msg.data
        if command == 'forward':
            print('Moving forward')
            self.wheelie.goForward()
        elif command == 'backward':
            print('Moving backward')
            self.wheelie.goBackward()
        elif command == 'left':
            print('Turning left')
            self.wheelie.goBackward()
        elif command == 'right':
            print('Turning right')
            self.wheelie.goRight()
        elif command == 'stop':
            print('Stopping')
            self.wheelie.stop()
        else:
            print('Unknown command, stopping instead')
            self.wheelie.stop()

def main(args=None):
    #  initialize the wheelie node
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()

    #  wait for incoming commands
    print('Initialized, waiting for command')
    rclpy.spin(minimal_subscriber)

    #  Interrupt detected, shut down
    minimal_subscriber.wheelie.stop()
    GPIO.cleanup()
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

