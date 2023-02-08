#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Pin Definitions
hall_input_pin_A = 23  
hall_input_pin_B = 24  

def main():
    
    
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BCM pin-numbering scheme from Raspberry Pi, BOARD for Jetson)
    GPIO.setup(hall_input_pin_A, GPIO.IN)  # set pin as an input pin
    GPIO.setup(hall_input_pin_B, GPIO.IN)
    
    val_A_pre = GPIO.input(hall_input_pin_A)
    val_A_curr = 0
    val_B_curr = 0
    angle_pos = 0
    count = 0
    try:
        while True:
            val_A_curr = GPIO.input(hall_input_pin_A)

            if val_A_curr != val_A_pre:
                val_B_curr = GPIO.input(hall_input_pin_B)
                if val_A_curr == 1:
                    if val_B_curr == 0:
                        angle_pos = angle_pos -1
                    else:
                        angle_pos = angle_pos +1
                else:
                    
                    if val_B_curr == 0:
                        angle_pos = angle_pos +1
                    else:
                        angle_pos = angle_pos -1
            print(angle_pos)

            val_A_pre = val_A_curr
            count += 1
            if count == 10000:
                count = 0
                f = open("hall_2_reading","w")
                f.write(str(angle_pos))
                f.close()
            
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
