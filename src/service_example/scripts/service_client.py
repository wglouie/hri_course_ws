#!/usr/bin/env python

import rospy
import sys

def add_two_ints_client(x,y):
    rospy.wait_for_service("adder_service")
    try:
        add_two_ints = rospy.ServiceProxy('adder_service', Adder)
        resp1 = add_two_ints(x,y)
        return resp1.result
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def usage():
    return "%s [x y]"%sys.argv[0]

from service_example.srv import *

if __name__ == '__main__':
    if(len(sys.argv) == 3):
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    print "Requesting %s+%s"%(x,y)
    print "%s + %s = %s"%(x,y, add_two_ints_client(x,y))