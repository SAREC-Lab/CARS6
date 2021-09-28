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
	v, delta = float(1), float(-0.9) # negative angle turns right
	dur = rospy.Duration(1.0)
    	rate = rospy.Rate(10)
    	start = rospy.Time.now()
	
	drive = AckermannDrive(steering_angle=delta, speed=v)

    	while rospy.Time.now() - start < dur:
		pub_controls.publish(AckermannDriveStamped(drive=drive))
		rate.sleep()
		
        return 'do_plan'
