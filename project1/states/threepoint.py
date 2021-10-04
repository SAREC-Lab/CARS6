#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from send_init_pos import send_init_pos

# Define three point turn state


class ThreePoint(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self,
                             outcomes=["do_plan"],
                             input_keys=["curr_state"])
        self.counter = 0
        self.pub_controls = pub_controls

    def execute(self, userdata):
        # get state attributes
        state_name = userdata.curr_state["name"]
        radius = userdata.curr_state["attributes"]["radius"]

        rospy.loginfo("Running {} state".format(state_name))
        v = [ 1, -1, 1]
        delta= [0.9, -0.9, 0.45]
	dur = [rospy.Duration(2.0), rospy.Duration(1.0), rospy.Duration(2.0)]
    	rate = rospy.Rate(10)
    	
	for x in range(3):
            start = rospy.Time.now()
            drive = AckermannDrive(steering_angle=delta[x], speed=v[x])
            while rospy.Time.now() - start < dur[x]:
                self.pub_controls.publish(AckermannDriveStamped(drive=drive))
                rate.sleep()
            time.sleep(0.5)
		
	
        return 'do_plan'
