cmake_minimum_required(VERSION 3.0.2)
project(motor_control)

find_package(catkin REQUIRED rospy std_msgs keyboard)
catkin_package(CATKIN_DEPENDS rospy std_msgs keyboard)
include_directories(${catkin_INCLUDE_DIRS})

catkin_install_python(PROGRAMS src/command_read_1.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
