#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from  ti_mmwave_rospkg.msg import RadarScan

HealthStatus = ['0', '0', '0', '0', '0', '0', '0']
sensortowers = ['uav', 'wamv', '_lidartower', '_zedtower_left', '_zedtower_mid', '_zedtower_right']
columns = ["H.B.","ZEDm","D435","LIDAR","mmWave","GPS","gripper"]

def callback_mmwave1(data):
    HealthStatus[4] = '4' *mmwave

def callback_zed(data):
    HealthStatus[0] = '1' #heartbeat
    HealthStatus[1] = '1' #zed_left

def listener():
    rospy.init_node('zedtower_left', anonymous=True)
    rospy.Subscriber("/wamv/zed_left/zed_node/rgb/image_rect_color", Image, callback_zed)
    rospy.Subscriber("/sensortower1/radar_2/ti_mmwave/ti_mmwave/radar_scan", RadarScan, callback_mmwave1)
    pub = rospy.Publisher('health/_zedtower_left', String, queue_size=10)
    while not rospy.is_shutdown():
        healthstring = '_zedtower_left@' + HealthStatus[0] + ':' + HealthStatus[1] + ':' + HealthStatus[2] + ':0:0:0:0'
        print(healthstring)
        pub.publish(healthstring)
        HealthStatus[0] = '0'
        HealthStatus[1] = '0'
        HealthStatus[2] = '0'
        rospy.sleep(1)

if __name__ == '__main__':
    print("start health status node\n")
    listener()
