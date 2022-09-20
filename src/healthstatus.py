#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image

HealthStatus = [0, 0]

def callback(data):
    HealthStatus[0] = 1
    
def listener():
    rospy.init_node('healthstatus', anonymous=True)
    rospy.Subscriber("/zed/zed_node/left_raw/image_raw_color", Image, callback)
    while not rospy.is_shutdown():
        print('Zed : ' + str(HealthStatus[0]) + '       mmwave : ' + str(HealthStatus[1]))
        HealthStatus[0] = 0
        HealthStatus[1] = 0
        rospy.sleep(2)

if __name__ == '__main__':
    print("start health status node\n")
    listener()
