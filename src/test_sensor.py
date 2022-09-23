#!/usr/bin/env python
import rospy
import pytest
from sensor_msgs.msg import Image
from std_msgs.msg import String

flag = False

def callback_zed(data):
    if data != NULL:
        flag = True

def listener():
    try:
        rospy.init_node('sensor_pytest', anonymous=True)
        rospy.Subscriber("/zed/zed_node/left_raw/image_raw_color", Image, callback_zed)
        flag = False
        rospy.sleep(5)
        assert flag
    except:
        assert False

def test_main():
    listener()
