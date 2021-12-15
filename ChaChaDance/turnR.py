#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from geometry_msgs.msg import Twist


# define state turnR - turn right
class TurnR(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self, outcomes=['do_plan'],
                            input_keys=['curr_state'])
        self.pub_controls = pub_controls
        self.counter = 0

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]

        rospy.loginfo("Running {} state".format(state_name))

        move_cmd = Twist()
        move_cmd.angular.z = -10
        
        rate = rospy.Rate(10)
        
        dur = rospy.Duration(3.5 / (7.0))
        t0 = rospy.Time.now()

        while rospy.Time.now() - t0 < dur:
            self.pub_controls.publish(move_cmd)
            rate.sleep()

        move_cmd = Twist()
        move_cmd.angular.z = 0.0
        self.pub_controls.publish(move_cmd)

        return "do_plan"
