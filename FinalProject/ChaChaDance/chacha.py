#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
import math
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

# Define circle state


class ChaCha(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self,
                             outcomes=["do_plan"],
                             input_keys=["curr_state"])
        self.counter = 0
        self.pub_controls = pub_controls

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]

        rospy.loginfo("Running {} state".format(state_name))

        while rospy.Time.now() - start < dur:
            self.pub_controls.publish(AckermannDriveStamped(drive=drive))
            rate.sleep()

        time.sleep(1)

        return "do_plan"