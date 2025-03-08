cmake_minimum_required(VERSION 2.8.3)
project(basic_example)
find_package(catkin REQUIRED COMPONENTS
  rospy
  message_generation
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_service_files(FILES Adder.srv)

generate_messages()

catkin_package()


