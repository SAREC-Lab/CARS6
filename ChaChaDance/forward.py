#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from geometry_msgs.msg import Twist


# Define forward state
class Forward(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self, outcomes=["do_plan"], input_keys=["curr_state"])
        self.counter = 0
        self.pub_controls = pub_controls

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]

        rospy.loginfo("Running {} state".format(state_name))

        dur = rospy.Duration(2.8 / (6.0))
        rate = rospy.Rate(10)
        start = rospy.Time.now()

        while rospy.Time.now() - start < dur:
            move_cmd = Twist()
            move_cmd.linear.x = 3.0
            self.pub_controls.publish(move_cmd)
            rate.sleep()

        move_cmd = Twist()
        move_cmd.linear.x = 0.0
        self.pub_controls.publish(move_cmd)

        return "do_plan"

