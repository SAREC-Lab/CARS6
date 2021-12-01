#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from geometry_msgs.msg import Twist
from moveturtle import Turtlebot
from maze_navigator import navigate
#Add states to library


# define state Stop
class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_exit'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('The turtle has stopped')
	time.sleep(1)
        return 'do_exit'


# Run bot
def runTurtleBot():
    rospy.init_node('squishy_turtlebot3')
    turtleBot = Turtlebot(namespace="squishy")
    
     # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['do_exit'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('TwistRight', TwistRight(), 
                               transitions={'do_twist_left':'TwistLeft'})

    #navigate(turtleBot)

    #rospy.spin()
    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    runTurtleBot()
