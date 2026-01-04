#!/usr/bin/env python
#
# BSD 3-Clause License
#
# This file is part of the Basalt project.
# https://gitlab.com/VladyslavUsenko/basalt.git
#
# Copyright (c) 2019-2021, Vladyslav Usenko and Nikolaus Demmel.
# All rights reserved.
#

import sys
import os
import rospy
from nav_msgs.msg import Odometry


def callback(data):
    global out_file, time_offset
    if not out_file:
        return

    if not time_offset:
        time_offset = rospy.Time().now() - data.header.stamp

    out_file.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n'.format(
        data.header.stamp + time_offset,
        data.pose.pose.position.x,
        data.pose.pose.position.y,
        data.pose.pose.position.z,
        data.pose.pose.orientation.x,
        data.pose.pose.orientation.y,
        data.pose.pose.orientation.z,
        data.pose.pose.orientation.w,
        data.twist.twist.linear.x,
        data.twist.twist.linear.y,
        data.twist.twist.linear.z,
        data.twist.twist.angular.x,
        data.twist.twist.angular.y,
        data.twist.twist.angular.z

    ))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/odom', Odometry, callback)

    rospy.spin()


if __name__ == '__main__':

    out_file = None
    time_offset = None

    out_file = open('/data.csv', 'w')
    out_file.write('#timestamp [ns], p_x [m], p_y [m], p_z [m], q_x [], q_y [], q_z [], q_w [], v_x [], v_y [], v_z [], rv_x [], rv_y [], rv_z []\n')
    listener()
    out_file.close()
