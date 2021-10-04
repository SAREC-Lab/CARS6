#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

# define state forward
class Forward(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self, outcomes=['do_plan'],
                             input_keys=['curr_state'])
        self.counter = 0 
        self.pub_controls = pub_controls

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]
        distance = userdata.curr_state["attributes"]["distance"]

        rospy.loginfo("Running {} state".format(state_name))
        
        velocity = 2.0  # default velocity
        delta = 0.0 # not turning so angle = 0

        dur = rospy.Duration(distance / velocity)
        rate = rospy.Rate(10)
        
        drive = AckermannDrive(steering_angle=delta, speed=velocity)
        start = rospy.Time.now()
        
        while(rospy.Time.now() - start < dur):
            self.pub_controls.publish(AckermannDriveStamped(drive=drive))
            rate.sleep()
               
        time.sleep(1)
        
        
        return 'do_plan'
