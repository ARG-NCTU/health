#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

def listener():
    rospy.init_node('zedtower_good', anonymous=True)
    pub_l = rospy.Publisher('health/zedtower_left', String, queue_size=10)
    pub_m = rospy.Publisher('health/zedtower_mid', String, queue_size=10)
    pub_r = rospy.Publisher('health/zedtower_right', String, queue_size=10)
    pub_lidar = rospy.Publisher('health/lidartower', String, queue_size=10)
    while not rospy.is_shutdown():
        healthstring = 'zedtower_left@' + str(1) + ':' + str(4) + ':' + str(0)
        pub_l.publish(healthstring)
        healthstring = 'zedtower_mid@' + str(1) + ':' + str(4) + ':' + str(0)
        pub_m.publish(healthstring)
        healthstring = 'zedtower_right@' + str(1) + ':' + str(4) + ':' + str(0)
        pub_r.publish(healthstring)
        healthstring = 'lidartower@' + str(0) + ':' + str(4) + ':' + str(1)
        pub_lidar.publish(healthstring)
        rospy.sleep(1)

if __name__ == '__main__':
    print("start health status node\n")
    listener()
