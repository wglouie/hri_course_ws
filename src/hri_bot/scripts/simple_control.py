#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class RedGreenLightBot:
    def __init__(self):
        rospy.init_node("red_light_green_light_bot")
        rospy.Timer(rospy.Duration(0.1),self.pub_drive_cmd)
        rospy.Timer(rospy.Duration(3),self.state_change_callback)

        self.cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=1)
        self.dog_pub = rospy.Publisher("dog", Twist, queue_size=1)

        self.green_light_state = True
        self.red_twist_msg = Twist()
        self.green_twist_msg = Twist()
        self.green_twist_msg.angular.z = 1
        rospy.spin()

    def pub_drive_cmd(self,event):
        if self.green_light_state:
            self.cmd_vel_pub.publish(self.green_twist_msg)
        else:
            self.cmd_vel_pub.publish(self.red_twist_msg)

    def state_change_callback(self,event):
        self.green_light_state = not self.green_light_state

if __name__ == "__main__":
    try:
        RedGreenLightBot()
    except rospy.ROSInterruptException:
        pass