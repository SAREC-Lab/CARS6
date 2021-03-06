#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

# Define the stop state


class Stop(smach.State):
    def __init__(self,  pub_controls):
        smach.State.__init__(self, outcomes=["do_exit"])
        self.counter = 0
        
        self.pub_controls = pub_controls

    def execute(self, userdata):
        rospy.loginfo("Running Stop state")

        delta = 0
        velocity = 0
        dur = rospy.Duration(5.0)
        rate = rospy.Rate(10)

        drive = AckermannDrive(steering_angle=delta, speed=velocity)
        start = rospy.Time.now()
        while rospy.Time.now() - start < dur:
            self.pub_controls.publish(AckermannDriveStamped(drive=drive))
            rate.sleep()

        time.sleep(1)

        return "do_exit"
