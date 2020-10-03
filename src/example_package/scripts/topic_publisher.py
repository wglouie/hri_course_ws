#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('/topic_out', String, queue_size=10)

def callback(data):
    new_string = String()
    new_string = data.data + "_123"
    pub.publish(new_string)

def listener():
    rospy.init_node('topic_publisher_example',anonymous=True)
    rospy.Subscriber('/topic_in',String,callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
