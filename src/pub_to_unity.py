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
        im = cv2.imread('/home/ezra/share_data/text.jpg', 1)
        # convert np image to grayscale
        featPoints = feat_det.detect(
            cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY))
        time2 = time.time()

        for featpoint in featPoints:
            x,y = featpoint.pt
            cv2.circle(image_np,(int(x),int(y)), 3, (0,0,255), -1)
        
        cv2.imshow('cv_img', image_np)
        cv2.waitKey(2)

        #### Create CompressedIamge ####
        msg = CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv2.imencode('.jpg', image_np)[1]).tostring()
        self.image_pub.publish(msg)

def main(args):
    '''Initializes and cleanup ros node'''
    ic = image_feature()
    rospy.init_node('pub_to_unity', anonymous=True)
    try:
        ic.run()
    except KeyboardInterrupt:
        print "Shutting down pub_to_unity node"
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
