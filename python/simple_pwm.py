#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

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
    
    try:
        while True:

            f = open("manual_control_data","r")
            num = f.read()
            if num == "119":
                #print("forward")
                # Straight/CW of Motor 1 for this setup
                GPIO.output(dir1_pin_1, GPIO.LOW)
                GPIO.output(dir2_pin_1, GPIO.HIGH)

                # Straight/CW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.HIGH)
                GPIO.output(dir2_pin_2, GPIO.LOW)
                val = 40
                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val)
            elif num =="100":
                GPIO.output(dir1_pin_1, GPIO.LOW)
                GPIO.output(dir2_pin_1, GPIO.HIGH)

                # CCW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.LOW)
                GPIO.output(dir2_pin_2, GPIO.HIGH)
                val = 30
                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val) 
            elif num =="97":
                print("lean right, rotate left")
                # CCW of Motor 1 for this setup
                GPIO.output(dir1_pin_1, GPIO.HIGH)
                GPIO.output(dir2_pin_1, GPIO.LOW)

                # CW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.HIGH)
                GPIO.output(dir2_pin_2, GPIO.LOW)
                val = 30
                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val)  
            elif num =="115":
                # Straight/CW of Motor 1 for this setup
                GPIO.output(dir1_pin_1, GPIO.HIGH)
                GPIO.output(dir2_pin_1, GPIO.LOW)

                # Straight/CW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.LOW)
                GPIO.output(dir2_pin_2, GPIO.HIGH)
                val = 40
                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val)                            
            else:
                # Straight/CW of Motor 1 for this setup
                GPIO.output(dir1_pin_1, GPIO.LOW)
                GPIO.output(dir2_pin_1, GPIO.HIGH)

                # Straight/CW of Motor 2 for this setup
                GPIO.output(dir1_pin_2, GPIO.HIGH)
                GPIO.output(dir2_pin_2, GPIO.LOW)
                val = 0
                p1.ChangeDutyCycle(val)
                p2.ChangeDutyCycle(val)
            f.close()
    finally:
        p1.stop()
        p2.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
