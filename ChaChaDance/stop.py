#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from geometry_msgs.msg import Twist


# Define the stop state
class Stop(smach.State):
    def __init__(self,  pub_controls):
        smach.State.__init__(self, outcomes=["do_exit"])
        self.counter = 0
        self.pub_controls = pub_controls

    def execute(self, userdata):
        rospy.loginfo("Running Stop state")

        move_cmd = Twist()
        move_cmd.linear.x = 0.0
        self.pub_controls.publish(move_cmd)

        time.sleep(1)

        return "do_exit"
