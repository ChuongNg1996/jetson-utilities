#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from keyboard.msg import Key

def callback_keydown(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.code)
    f = open("manual_control_data","w")
    f.write(str(data.code))
    f.close()

def callback_keyup(data):
    f = open("manual_control_data","w")
    f.write("stop")
    f.close()
    

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/keyboard/keydown", Key, callback_keydown)
    rospy.Subscriber("/keyboard/keyup", Key, callback_keyup)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
