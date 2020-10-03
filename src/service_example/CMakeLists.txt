cmake_minimum_required(VERSION 2.8.3)

project(service_example)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_service_files(
  FILES
  Adder.srv
)

generate_messages()
catkin_package()
