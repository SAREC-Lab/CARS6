#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
import math
from geometry_msgs.msg import Twist


# Define circle state
class Circle(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self, outcomes=["do_plan"], input_keys=["curr_state"])
        self.counter = 0
        self.pub_controls = pub_controls

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]
        direction = userdata.curr_state["direction"]

        rospy.loginfo("Running {} state".format(state_name))

        dur = rospy.Duration(47 / (70.0))
        rate = rospy.Rate(10)

        move_cmd = Twist()
        move_cmd.linear.x= 5
        move_cmd.angular.z = 5 * direction

        t0=rospy.Time.now()
        while rospy.Time.now() - t0 < dur:
            self.pub_controls.publish(move_cmd)
            rate.sleep()

        #After the loop, stops the robot
        move_cmd = Twist()
        move_cmd.angular.z = 0
        move_cmd.linear.x = 0
        self.pub_controls.publish(move_cmd)

        return "do_plan"
    
