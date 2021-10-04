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
                             outcomes=["do_plan"], # outcome of the state once it completes
                             input_keys=["curr_state"])
        self.counter = 0
        self.pub_controls = pub_controls

    def execute(self, userdata): 
        # get state attributes
        state_name = userdata.curr_state["name"]

        rospy.loginfo("Running {} state".format(state_name))
	# Variable arrays that will be used for step 1-3 in three point turns
        v = [ 1, -1, 1] #velocity
        delta= [0.9, -0.9, 0.08] #turn left, turn backwards right, move forward left at slight angle
	dur = [rospy.Duration(1.8), rospy.Duration(1.0), rospy.Duration(2.0)] #duration of steps
    	rate = rospy.Rate(10) 
    	
	for x in range(3): # for loop interates through arrays and completes each step of 3 point turn
            start = rospy.Time.now()
            drive = AckermannDrive(steering_angle=delta[x], speed=v[x])
            while rospy.Time.now() - start < dur[x]:
                self.pub_controls.publish(AckermannDriveStamped(drive=drive)) # pulish drive command to car
                rate.sleep()
            time.sleep(0.5)
		
	# go to the next state which is "do_plan"
        return 'do_plan'
