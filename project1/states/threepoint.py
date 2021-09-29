#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from send_init_pos import send_init_pos

# Define three point turn state


class ThreePoint(smach.State):
    def __init__(self, pub_init_pos, pub_controls):
        smach.State.__init__(self,
                             outcomes=["do_plan"],
                             input_keys=["curr_state"])
        self.counter = 0
        self.pub_init_pos = pub_init_pos
        self.pub_controls = pub_controls

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]
        radius = userdata.curr_state["attributes"]["radius"]

        rospy.loginfo("Running {} state".format(state_name))
