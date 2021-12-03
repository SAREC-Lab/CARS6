#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist


# define state TwistRight
class TurnR(smach.State):
    def __init__(self, pub_controls):
        smach.State.__init__(self, outcomes=['do_plan'],
			    input_keys=["curr_state"])
        self.counter = 0
	

    def execute(self, userdata):
		rospy.loginfo('The turtle is twisting right')
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # Set Twist to twist right
        vel_msg = Twist()
        vel_msg.linear.x=0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -10

        # Setup time to twist
        t0=rospy.Time.now().to_sec()
        t1=rospy.Time.now().to_sec()

        while(t1-t0<3):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()

		#After the loop, stops the robot
        vel_msg.angular.z = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

        return 'do_plan'