#!/usr/bin/env python
import rospy
import pytest
from sensor_msgs.msg import Image
from std_msgs.msg import String


def callback_zed(data):
    assert True

def listener():
    rospy.init_node('sensor_pytest', anonymous=True)
    rospy.Subscriber("/zed/zed_node/left_raw/image_raw_color", Image, callback_zed)
    rospy.sleep(5)
    assert False

def test_main():
    print("start health status test node\n")
    listener()
