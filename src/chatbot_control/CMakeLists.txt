cmake_minimum_required(VERSION 2.8.3)
project(chatbot_control)
find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
  dialogflow_ros
  dialogflow_ros_msgs
  geometry_msgs
  std_msgs
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

generate_messages()

catkin_package()

catkin_install_python(PROGRAMS scripts/chatbot_control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
