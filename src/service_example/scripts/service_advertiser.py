#!/usr/bin/env python

import rospy
from service_example.srv import Adder, AdderResponse

def callback(req):
  return AdderResponse(req.val1 + req.val2)

def add_two_ints_server():
  rospy.init_node("Adder_Advertiser")
  srv = rospy.Service("adder_service", Adder, callback)
  rospy.loginfo("Ready to run the service")
  rospy.spin()

if __name__ == "__main__":
  add_two_ints_server()
