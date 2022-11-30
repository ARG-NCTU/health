#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image, LaserScan
from std_msgs.msg import String
from  ti_mmwave_rospkg.msg import RadarScan

HealthStatus = ['0', '0', '0', '0', '0', '0', '0']
sensortowers = ['uav', 'wamv', '_lidartower', '_zedtower_left', '_zedtower_mid', '_zedtower_right']
columns = ["H.B.","ZEDm","D435","LIDAR","mmWave","GPS","gripper"]

def callback_mmwave1(data):
    HealthStatus[4] = '4' #mmwave

def callback_lidar(data):
    HealthStatus[0] = '1' #heartbeat
    HealthStatus[3] = 1 #lidar
    
def listener():
    rospy.init_node('lidartower', anonymous=True)
    rospy.Subscriber("/wamv/RL/scan", LaserScan, callback_lidar)
    rospy.Subscriber("/lidartower/radar_2/ti_mmwave/ti_mmwave/radar_scan", RadarScan, callback_mmwave1)
    pub = rospy.Publisher('health/_lidartower', String, queue_size=10)
    while not rospy.is_shutdown():
        healthstring = '_lidartower@' + (HealthStatus[0]) + ':0:0:' + HealthStatus[3] + ':' + HealthStatus[4] + ':0:0'
        print(healthstring)
        pub.publish(healthstring)
        HealthStatus[0] = '0'
        HealthStatus[3] = '0'
        HealthStatus[4] = '0'
        rospy.sleep(1)

if __name__ == '__main__':
    print("start health status node\n")
    listener()
