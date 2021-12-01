#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from send_init_pos import send_init_pos

# Define planning state


class Plan(smach.State):
    def __init__(self, pub_init_pos):
        smach.State.__init__(self, outcomes=["do_circleL", "do_circleR", "do_turnL", "do_turnR", "do_forward", "do_backward", "do_chacha", "do_clap" "do_exit"],
                             input_keys=["plan", "curr_state", "plan_length"],
                             output_keys=["curr_state"])

        self.pub_init_pos = pub_init_pos
        self.counter = 0

    def execute(self, userdata):
        # if plan is empty, exit
        if not userdata.plan:
            return 'do_exit'

        # if first state, set initial pos
        if userdata.plan_length == len(userdata.plan):
            send_init_pos(self.pub_init_pos)

        # get the first state
        current_state = userdata.plan.pop(0)
        userdata.curr_state = current_state
        rospy.loginfo("Planning attempting to run: {}"
                      .format(current_state["name"]))

        time.sleep(1)

        return current_state["name"]