#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist

# define state turnL - turn left
class TurnR(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_plan'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle is turning right')
	time.sleep(2)
        return 'do_plan'
