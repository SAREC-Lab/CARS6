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
        move_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10) #might need to add turtle name

        # Set Twist to twist right
        move_cmd = Twist()
        move_cmd.linear.x=0
        move_cmd.linear.y = 0
        move_cmd.linear.z = 0
        move_cmd.angular.x = 0
        move_cmd.angular.y = 0
        move_cmd.angular.z = -10

        # Setup time to twist
        t0=rospy.Time.now().to_sec()
        t1=rospy.Time.now().to_sec()

        while(t1-t0<3):
            #Publish the move
            move_publisher.publish(move_cmd)
            t1=rospy.Time.now().to_sec()

		#After the loop, stops the robot
        move_cmd.angular.z = 0
        #Force the robot to stop
        move_publisher.publish(move_cmd)

        return 'do_plan'