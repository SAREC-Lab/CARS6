#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time

# Define the stop state


class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=["do_exit"])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo("Running stop state")

        time.sleep(1)

        return "do_exit"
