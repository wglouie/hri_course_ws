#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from dialogflow_ros.msg import DialogflowResult

pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)

def callback(data):
    print data.intent
    if data.intent == 'move':
        twist_msg = Twist()
        print data.parameters[0].value[0]

        if 'Right' in data.parameters[0].value[0]:
            twist_msg.angular.z = 5
        elif 'Left' in data.parameters[0].value[0]:
            twist_msg.angular.z = -5
        elif 'Up' in data.parameters[0].value[0]:
            twist_msg.linear.x = 5
        elif 'Down' in data.parameters[0].value[0]:
            twist_msg.linear.x = -5
        else:
            print "No movement direction provided by users"
            return
        print twist_msg
        pub.publish(twist_msg)
        
def listener():
    rospy.init_node('chatbot_control',anonymous=True)
    rospy.Subscriber('/dialogflow_client/results', DialogflowResult, callback)
    rospy.spin()

if __name__=='__main__':
    try:
        listener()
    except rospy.InterrupException:
        pass

