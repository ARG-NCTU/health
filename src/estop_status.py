#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Bool
import time

estop_status = True

def callback(data):
    global estop_status
    estop_status = False
    
def listener():
    global estop_status
    rospy.init_node('estop_status', anonymous=True)
    rospy.Subscriber("/joy", Joy, callback)
    pub = rospy.Publisher('stop_state', Bool, queue_size=10)
    estop_status = True
    while not rospy.is_shutdown():
        if estop_status == True:
            print("estop_status is : " + str(estop_status))
            pub.publish(estop_status)
        else:
            estop_status = True
        rospy.sleep(2)

if __name__ == '__main__':
    print("start estop status node\n")
    listener()
