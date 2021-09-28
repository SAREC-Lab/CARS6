#!/usr/bin/env python

# Import libraries
import rospy
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from plan_parser import parse_plan
from state_machine import run_state_machine


def run_plan(pub_init_pose, pub_controls, plan):
    print("running plan...")
    run_state_machine(pub_init_pose, pub_controls, plan)


if __name__ == '__main__':
    rospy.init_node("path_publisher")

    control_topic = rospy.get_param(
        "~control_topic", "/car/mux/ackermann_cmd_mux/input_navigation")
    pub_controls = rospy.Publisher(
        control_topic, AckermannDriveStamped, queue_size=1)

    init_pose_topic = rospy.get_param("~init_pose_topic", "/initialpose")
    pub_init_pose = rospy.Publisher(
        init_pose_topic, PoseWithCovarianceStamped, queue_size=1)

    plan_file = rospy.get_param("~plan_file")
    plan = parse_plan(plan_file)

    rospy.sleep(1.0)
    run_plan(pub_init_pose, pub_controls, plan)
