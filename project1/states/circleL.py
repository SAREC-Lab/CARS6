#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
import math
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

# Define circle left state
class CircleL(smach.State):
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

        # set initial state position
        send_init_pos(state_name, self.pub_init_pos)

        l = 0.785
        delta = math.asin(l / (2 * radius))
        velocity = 2.0  # default velocity

        c = 2 * math.pi * radius
        dur = rospy.Duration((c / velocity))
        rate = rospy.Rate(10)

        drive = AckermannDrive(steering_angle=delta, speed=velocity)
        start = rospy.Time.now()
        while rospy.Time.now() - start < dur:
            self.pub_controls.publish(AckermannDriveStamped(drive=drive))
            rate.sleep()

        time.sleep(1)

        return "do_plan"
