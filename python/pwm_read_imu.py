#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import re

pwm_pin_1 = 32
dir1_pin_1 = 31
dir2_pin_1 = 29

pwm_pin_2 = 33
dir1_pin_2 = 35
dir2_pin_2 = 36

if pwm_pin_1 is None:
    raise Exception('PWM not supported on this board')

if pwm_pin_2 is None:
    raise Exception('PWM not supported on this board')

def main():
    # Pin Setup:
    # Board pin-numbering scheme
    GPIO.setmode(GPIO.BOARD)
    # set pin as an output pin with optional initial state of HIGH
    GPIO.setup(dir1_pin_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(dir2_pin_1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(dir1_pin_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(dir2_pin_2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pwm_pin_1, GPIO.OUT, initial=GPIO.HIGH)
    p1 = GPIO.PWM(pwm_pin_1, 50)
    val = 0
    p1.start(val)

    GPIO.setup(pwm_pin_2, GPIO.OUT, initial=GPIO.HIGH)
    p2 = GPIO.PWM(pwm_pin_2, 50)
    p2.start(val)

    print("PWM running. Press CTRL+C to exit.")
    val = 65
    try:
        while True:
            f = open("imu_data","r")
            num = f.read()
            if len(num) != 0:
                if num[0] == '-':
                    num_array = re.findall(r'-\d+.\d+',num)
                else:
                    num_array = re.findall(r'\d+.\d+',num)
                value = float(num_array[0])

            print(value)
            if value < -5.0:
                print("lean right, rotate left")
                # CCW of Motor 1 for this setup
                GPIO.output(dir1_pin_1, GPIO.HIGH)
                GPIO.output(dir2_pin_1, GPIO.LOW)

                # CW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.HIGH)
                GPIO.output(dir2_pin_2, GPIO.LOW)

                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val)   
            elif value > 5.0:
                print("lean left, rotate right")
                # CW of Motor 1 for this setup
                GPIO.output(dir1_pin_1, GPIO.LOW)
                GPIO.output(dir2_pin_1, GPIO.HIGH)

                # CCW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.LOW)
                GPIO.output(dir2_pin_2, GPIO.HIGH)

                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val)                            
            else:
                print("go straight")

                # Straight/CW of Motor 1 for this setup
                GPIO.output(dir1_pin_1, GPIO.LOW)
                GPIO.output(dir2_pin_1, GPIO.HIGH)

                # Straight/CW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.HIGH)
                GPIO.output(dir2_pin_2, GPIO.LOW)

                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val)
            f.close()
    finally:
        p1.stop()
        p2.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
