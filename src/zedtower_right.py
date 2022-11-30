#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String

HealthStatus = ['0', '0', '0', '0', '0', '0', '0']
sensortowers = ['uav', 'wamv', '_lidartower', '_zedtower_left', '_zedtower_mid', '_zedtower_right']
columns = ["H.B.","ZEDm","D435","LIDAR","mmWave","GPS","gripper"]

def callback_zed(data):
    HealthStatus[0] = '1' #heartbeat
    HealthStatus[1] = '1' #zed_right
    
def listener():
    rospy.init_node('zedtower_right', anonymous=True)
    rospy.Subscriber("/wamv/zed_right/zed_node/rgb/image_rect_color", Image, callback_zed)
    pub = rospy.Publisher('health/_zedtower_right', String, queue_size=10)
    while not rospy.is_shutdown():
        healthstring = '_zedtower_right@' + HealthStatus[0] + ':' + HealthStatus[1] + ':' + HealthStatus[2] + ':0:0:0:0'
        print(healthstring)
        pub.publish(healthstring)
        HealthStatus[0] = '0'
        HealthStatus[1] = '0'
        HealthStatus[2] = '0'
        rospy.sleep(1)

if __name__ == '__main__':
    print("start health status node\n")
    listener()
