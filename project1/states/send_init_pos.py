#!/usr/bin/env python

# Import libraries
import rospy
from geometry_msgs.msg import (
    Pose,
    Point,
    Quaternion,
    PoseWithCovariance,
    PoseWithCovarianceStamped,
)
from tf.transformations import quaternion_from_euler


def send_init_pos(state_name, pub_init_pos, x=0, y=0, theta=0):
    rospy.loginfo("Setting initial positon for: {}".format(state_name))
    q = Quaternion(*quaternion_from_euler(0, 0, theta))
    point = Point(x=x, y=y)
    pose = PoseWithCovariance(pose=Pose(position=point, orientation=q))
    pub_init_pos.publish(PoseWithCovarianceStamped(pose=pose))
