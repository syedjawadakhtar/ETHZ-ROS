#! /usr/bin/env python

import rospy
from sensor_msgs.msgs import LaserScan

def callback():
	print len(msg.ranges)

rospy.init_node('las_scan')
sub = rospy.subscriber('/husk_high_level_controller/laser/scan', LaserScan, callback)
rospy.spin()