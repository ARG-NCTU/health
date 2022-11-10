#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

sensortowers = ['uav', 'wamv', '_lidartower', '_zedtower_left', '_zedtower_mid', '_zedtower_right']
columns = ["H.B.","ZEDm","D435","LIDAR","mmWave","GPS","gripper"]

def listener():
    rospy.init_node('zedtower_good', anonymous=True)
    pub_uav = rospy.Publisher('health/uav', String, queue_size=10)
    pub_wamv = rospy.Publisher('health/wamv', String, queue_size=10)
    pub_lidar = rospy.Publisher('health/_lidartower', String, queue_size=10)
    pub_l = rospy.Publisher('health/_zedtower_left', String, queue_size=10)
    pub_m = rospy.Publisher('health/_zedtower_mid', String, queue_size=10)
    pub_r = rospy.Publisher('health/_zedtower_right', String, queue_size=10)
    while not rospy.is_shutdown():
        healthstring = sensortowers[0] + '@1:1:1:0:0:1:1'
        pub_uav.publish(healthstring)
        healthstring = sensortowers[1] + '@1:0:0:0:0:1:0'
        pub_wamv.publish(healthstring)
        healthstring = sensortowers[2] + '@1:0:0:1:1:1:0'
        pub_lidar.publish(healthstring)
        healthstring = sensortowers[3] + '@1:1:0:0:1:1:0'
        pub_l.publish(healthstring)
        healthstring = sensortowers[4] + '@1:1:0:0:1:1:0'
        pub_m.publish(healthstring)
        healthstring = sensortowers[5] + '@1:1:0:0:1:1:0'
        pub_r.publish(healthstring)
        rospy.sleep(1)

if __name__ == '__main__':
    print("start health status node\n")
    listener()
