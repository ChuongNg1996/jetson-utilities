#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import threading
import datetime

R = 3.5/100
D = 20.0/100

global w1_pos
global w2_pos
w1_pos = 0
w2_pos = 0

import rospy
from std_msgs.msg import String

def hall_1():
    global w1_pos
    f = open("hall_1_reading","r")
    hall_1_pre = f.read()
    f.close()
    t_pre = datetime.datetime.now()
    #print(hall_1_pre)
    lin_p = 0
    while True:
        f = open("hall_1_reading","r")
        hall_1_curr = f.read()
        f.close()
        if hall_1_curr != hall_1_pre:
            if hall_1_curr != '':
                #print(hall_1_curr)
                t_curr = datetime.datetime.now()
                t_diff = t_curr - t_pre
                t_pre = t_curr
                # print(t_diff.total_seconds())
                lin_p += ((int(hall_1_curr) - int(hall_1_pre))*3.14/180*R)*t_diff.total_seconds()
                print(lin_p)
                w1_pos = lin_p
                hall_1_pre = hall_1_curr


def hall_2():
    global w2_pos
    f = open("hall_2_reading","r")
    hall_2_pre = f.read()
    f.close()
    t_pre = datetime.datetime.now()
    #print(hall_2_pre)
    lin_p = 0
    while True:
        f = open("hall_2_reading","r")
        hall_2_curr = f.read()
        f.close()
        if hall_2_curr != hall_2_pre:
            if hall_2_curr != '':
                #print(hall_2_curr)
                t_curr = datetime.datetime.now()
                t_diff = t_curr - t_pre
                t_pre = t_curr
                 # print(t_diff.total_seconds())
                lin_p += ((int(hall_2_curr) - int(hall_2_pre))*3.14/180*R)*t_diff.total_seconds()
                print(lin_p)
                w2_pos = lin_p
                hall_2_pre = hall_2_curr

def main():
    try:
        
        global w1_pos
        global w2_pos
        hall_1_th = threading.Thread(target=hall_1)
        hall_1_th.start()
        hall_2_th = threading.Thread(target=hall_2)
        hall_2_th.start()
        rospy.init_node('hall_data', anonymous=True)
        hall_pub = rospy.Publisher('hall_data',String, queue_size = 10)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            total_lin = (w1_pos + w2_pos)/2
            total_angle = (w1_pos - w2_pos)/D
            ros_msg = str(total_lin) + ' ' + str(total_angle)
            hall_pub.publish(ros_msg)
            print('ros_msg')
            rate.sleep()
            
    finally:
        pass

if __name__ == '__main__':
    main()