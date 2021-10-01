#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

# define state turnL - turn left
class TurnR(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self, outcomes=['do_plan'],
			    input_keys=["curr_state"])
        self.counter = 0
	
	self.pub_controls = pub_controls


    def execute(self, userdata):
	# get state attributes
        state_name = userdata.curr_state["name"]
        rospy.loginfo("Running {} state".format(state_name))
	
	v, delta = float(1), float(-0.9) # negative angle turns right
	dur = rospy.Duration(2.0)
    	rate = rospy.Rate(10)
    	start = rospy.Time.now()
	
	drive = AckermannDrive(steering_angle=delta, speed=v)
	

    	while rospy.Time.now() - start < dur:
		self.pub_controls.publish(AckermannDriveStamped(drive=drive))
		rate.sleep()
		
        return 'do_plan'
