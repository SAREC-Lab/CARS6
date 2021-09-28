#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist

# define state forward
class Forward(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_plan'])
        self.counter = 0

    def execute(self, userdata):

        velocity_publisher = rospy.Publisher(', Twist, queue_size=10)

        t0=rospy.Time.now().to_sec()
        t1=rospy.Time.now().to_sec()

        while(t1-t0<2):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()          
         
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        return 'do_plan'
