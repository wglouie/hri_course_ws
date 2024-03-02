cmake_minimum_required(VERSION 2.8.3)

project(chatbot_control)

find_package(catkin REQUIRED COMPONENTS
  dialogflow_ros
  geometry_msgs
  roscpp
  rospy
  std_msgs
  dialogflow_ros_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
catkin_package()

catkin_install_python(PROGRAMS scripts/chatbot_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
