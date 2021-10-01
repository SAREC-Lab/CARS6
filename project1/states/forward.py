#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from send_init_pos import send_init_pos

# define state forward
class Forward(smach.State):
    def __init__(self, pub_init_pos, pub_controls):
        smach.State.__init__(self, outcomes=['do_plan'], input_keys=['curr_state'])
        self.counter = 0 
        self.pub_init_pos = pub_init_pos
        self.pub_controls = pub_controls

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]
        distance = userdata.curr_state["attributes"]["distance"]

        rospy.loginfo("Running {} state".format(state_name))
        
        # set initial state position
        send_init_pos(state_name, self.pub_init_pos)

        velocity = 2.0  # default velocity
        delta = 0.0 # not turning so angle = 0

        dur = rospy.Duration(distance / velocity)
        rate = rospy.Rate(10)
        
        drive = AckermannDrive(steering_angle=delta, speed=velocity)
        start = rospy.Time.now()
        
        while(rospy.Time.now() - start < dur):
            self.pub_controls.publish(AckermannDriveStamped(drive=drive))
            rate.sleep()
           
            #Publish the velocity
            #velocity_publisher.publish(vel_msg)
               
        time.sleep(1)
        
        
        return 'do_plan'
