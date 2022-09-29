#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image, LaserScan
from std_msgs.msg import String
from  ti_mmwave_rospkg.msg import RadarScan

HealthStatus = [0, 0, 0]

def callback_mmwave1(data):
    HealthStatus[1] = 1

def callback_lidar(data):
    HealthStatus[2] = 1
    
def listener():
    rospy.init_node('sensortower4', anonymous=True)
    rospy.Subscriber("/wamv/RL/scan", LaserScan, callback_lidar)
    rospy.Subscriber("/lidartower/radar_2/ti_mmwave/ti_mmwave/radar_scan", RadarScan, callback_mmwave1)
    pub = rospy.Publisher('health/sensortower4', String, queue_size=10)
    while not rospy.is_shutdown():
        healthstring = 'sensortower4@' + str(HealthStatus[0]) + ':' + str(HealthStatus[1]) + ':' + str(HealthStatus[2])
        print(healthstring)
        pub.publish(healthstring)
        HealthStatus[0] = 0
        HealthStatus[1] = 0
        HealthStatus[2] = 0
        rospy.sleep(1)

if __name__ == '__main__':
    print("start health status node\n")
    listener()
