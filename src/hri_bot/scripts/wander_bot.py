#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class WanderBot:
    def __init__(self):
        rospy.init_node("wander_bot")
        rospy.Timer(rospy.Duration(5), self.change_state_callback)
        rospy.Timer(rospy.Duration(0.1), self.cmd_vel_pub_callback)

        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.scan_sub = rospy.Subscriber('scan', LaserScan, self.scan_callback)
        self.g_range_ahead = -1
        self.driving_forward = True
        self.twist = Twist()
        rospy.spin()

    def scan_callback(self, scan_msg):
        self.g_range_ahead = min(scan_msg.ranges)
        if(self.g_range_ahead < 0.8):
            self.driving_forward = False

    def change_state_callback(self, event):
        self.driving_forward = not self.driving_forward

    def cmd_vel_pub_callback(self, event):
        if self.driving_forward:
            self.twist.linear.x = 1
            self.twist.angular.z = 0
        else:
            self.twist.linear.x = 0
            self.twist.angular.z = 1

        self.cmd_vel_pub.publish(self.twist)

if __name__ == '__main__':

    try:
        WanderBot()
    except rospy.ROSInterruptException:
        pass
