#!/usr/bin/env python
import rospy, cv2, cv_bridge, numpy
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

class FollowBot:
    def __init__(self):
        rospy.init_node('follower')
        self.bridge = cv_bridge.CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.image_callback)
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel_mux/input/teleop", Twist, queue_size=1)
        self.twist = Twist()
        rospy.spin()

    def image_callback(self,msg):
        image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')

        #Masking the yellow out of the image
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        lower_yellow = numpy.array([10, 10, 10])
        upper_yellow = numpy.array([255, 255, 250])
        mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
        #Remove 20 row section
        h, w, d = image.shape
        search_top = 3*h/4
        search_bottom = 3*h/4 + 20
        mask[0:search_top, 0:w] = 0
        mask[search_bottom:h, 0:w] = 0
        cv2.imshow("mask", mask)

        #Calculate centroid of the yellow line
        M = cv2.moments(mask)
        if M['m00'] > 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.circle(image,(cx,cy), 20, (0,0,255), -1)

            #Begin calculating the control for the robot
            err = cx - w/2
            self.twist.linear.x = 0.2
            self.twist.angular.z = -err/100
            self.cmd_vel_pub.publish(self.twist)

        cv2.imshow("Debugging",image)
        cv2.waitKey(3)

if __name__ == "__main__":
    try:
        FollowBot()
    except rospy.ROSInterruptException:
        pass