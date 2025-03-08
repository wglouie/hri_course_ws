#!/usr/bin/env python3

from basic_example.srv import Adder, AdderResponse
import rospy

def srv_callback(req):
  return AdderResponse(req.val1 + req.val2)

def add_two_ints_server():
  rospy.init_node("service_advertiser")
  srv = rospy.Service('adder_service', Adder, srv_callback)
  rospy.spin()

if __name__ == "__main__":
  add_two_ints_server()