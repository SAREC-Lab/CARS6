#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
import math
from geometry_msgs.msg import Twist

def move_circle(pub_controls, direction):
    rospy.loginfo("Running circle state. Direction: {}".format(direction))

    dur = rospy.Duration(47 / (20.0))
    rate = rospy.Rate(10)

    move_cmd = Twist()
    move_cmd.linear.x= 5
    move_cmd.angular.z = 5 * direction

    t0=rospy.Time.now()
    while rospy.Time.now() - t0 < dur:
        pub_controls.publish(move_cmd)
        rate.sleep()

    #After the loop, stops the robot
    move_cmd = Twist()
    move_cmd.angular.z = 0
    move_cmd.linear.x = 0
    pub_controls.publish(move_cmd)

def move_forward(pub_controls, direction):
    rospy.loginfo("Running forward state. Direction: {}".format(direction))

    dur = rospy.Duration(10.8 / (6.0))
    rate = rospy.Rate(10)
    start = rospy.Time.now()

    while rospy.Time.now() - start < dur:
        move_cmd = Twist()
        move_cmd.linear.x = 3.0 * direction
        pub_controls.publish(move_cmd)
        rate.sleep()

    move_cmd = Twist()
    move_cmd.linear.x = 0.0
    pub_controls.publish(move_cmd)

def move_left(pub_controls):
    rospy.loginfo("Running left state.")

    move_cmd = Twist()
    move_cmd.angular.z = 10

    rate = rospy.Rate(10)

    dur = rospy.Duration(3.5 / (7.0))
    t0 = rospy.Time.now()

    while rospy.Time.now() - t0 < dur:
        pub_controls.publish(move_cmd)
        rate.sleep()

    move_cmd = Twist()
    move_cmd.angular.z = 0.0
    pub_controls.publish(move_cmd)

def move_right(pub_controls):
    rospy.loginfo("Running left state.")

    move_cmd = Twist()
    move_cmd.angular.z = -10

    rate = rospy.Rate(10)

    dur = rospy.Duration(3.5 / (7.0))
    t0 = rospy.Time.now()

    while rospy.Time.now() - t0 < dur:
        pub_controls.publish(move_cmd)
        rate.sleep()

    move_cmd = Twist()
    move_cmd.angular.z = 0.0
    pub_controls.publish(move_cmd)
