#!/usr/bin/env python
import sys, time
import numpy as np
from scipy.ndimage import filters
import cv2
import roslib
import rospy
from sensor_msgs.msg import CompressedImage

class image_feature:

    def __init__(self):
        '''Initialize ros publisher, ros subscriber'''
        self.image_pub = rospy.Publisher("/dts_health/image_raw/compressed",CompressedImage)

    def run(self):
        im = cv2.imread('/home/argduckiepond/share_data/text.jpg', 1)
        msg = CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv2.imencode('.jpg', im)[1]).tostring()
        self.image_pub.publish(msg)

def main(args):
    '''Initializes and cleanup ros node'''
    ic = image_feature()
    rospy.init_node('pub_to_unity', anonymous=True)
    while True:
        ic.run()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
