#!/usr/bin/env python

import rospy
from apriltag_ros.msg import AprilTagDetectionArray

x = 0.0
y = 0.0
z = 0.0

def tagDetect(msg):
    global x, y, z
    x = msg.detections[0].pose.pose.pose.position.x
    y = msg.detections[0].pose.pose.pose.position.y
    z = msg.detections[0].pose.pose.pose.position.z  
    rospy.loginfo("x = %s, y = %s, z = %s", x, y, z)

def listener():
    rospy.init_node("listener",anonymous=True)
    rospy.Subscriber("/tag_detections",AprilTagDetectionArray,tagDetect)    
    rospy.spin()

if __name__ == '__main__':
    listener()
