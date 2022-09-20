#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

HealthStatus = [0, 0]

def callback_zed(data):
    HealthStatus[0] = 1
    
def listener():
    rospy.init_node('sensortower2', anonymous=True)
    rospy.Subscriber("/zed/zed_node/left_raw/image_raw_color", Image, callback_zed)
    pub = rospy.Publisher('health/sensortower2', String, queue_size=10)
    while not rospy.is_shutdown():
        healthstring = 'sensortower2@' + str(HealthStatus[0]) + ':' + str(HealthStatus[1])
        print(healthstring)
        pub.publish(healthstring)
        HealthStatus[0] = 0
        HealthStatus[1] = 0
        rospy.sleep(1)

if __name__ == '__main__':
    print("start health status node\n")
    listener()