cmake_minimum_required(VERSION 2.8.3)

project(chatbot_control)

find_package(catkin REQUIRED COMPONENTS
  dialogflow_ros
  geometry_msgs
  roscpp
  rospy
  std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
catkin_package()
