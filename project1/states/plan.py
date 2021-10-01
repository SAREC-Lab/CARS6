#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time

# Define planning state


class Plan(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=["do_circleL", "do_circleR", "do_turnL", "do_exit"],
                             input_keys=["plan", "curr_state"],
                             output_keys=["curr_state"])
        self.counter = 0

    def execute(self, userdata):
        # if plan is empty, exit
        if not userdata.plan:
            return 'do_exit'

        # get the first state
        current_state = userdata.plan.pop(0)
        userdata.curr_state = current_state
        rospy.loginfo("Planning attempting to run: {}"
                      .format(current_state["name"]))

        time.sleep(1)

        return current_state["name"]
