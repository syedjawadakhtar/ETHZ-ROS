#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    rospy.loginfo (msg.ranges)

def scan():
	rospy.init_node('las_scan', anonymous=True)
	# topicname = rospy.get_param('~topic')
	# queuesize = rospy.get_param( '~queue')
	sub = rospy.Subscriber(name=sensor_msgs, data_class=LaserScan, callback=callback, queue_size= queuesize)
	rospy.spin()
	

if __name__ == '__main__':
	scan()