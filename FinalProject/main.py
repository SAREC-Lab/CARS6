#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
from geometry_msgs.msg import Twist
from moveturtle import Turtlebot
from maze_navigator import navigate
#Add states to library
from ChaChaDance.forward import Forward
from ChaChaDance.backward import Backward
from ChaChaDance.circle import Circle
from ChaChaDance.clap import Clap
from ChaChaDance.chacha import Chacha
from ChaChaDance.turnL import TurnL
from ChaChaDance.turnR import TurnR
from ChaChaDance.plan import Plan


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
        smach.StateMachine.add('Plan', Plan(), 
                               transitions={'do_forward':'Forward', 'do_backward': 'Backward', 'do_circle':'Circle', 
					    'do_turnL':'TurnL', 'do_turnR':'TurnR','do_clap':'Clap','do_chacha':'Chacha','do_exit':'Stop'})
        smach.StateMachine.add('Forward', Forward(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('Backward', Backward(), 
                                transitions={'do_plan':'Plan'})
        smach.StateMachine.add('Circle', Circle(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('TurnL', TurnL(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('TurnR', TurnR(), 
                               transitions={'do_plan':'Plan'})
	smach.StateMachine.add('Clap', Clap(), 
                               transitions={'do_clap':'Clap'})
	smach.StateMachine.add('Chacha', Chacha(), 
                               transitions={'do_chacha':'Chacha'})
        smach.StateMachine.add('Stop', Stop(), 
                               transitions={'do_exit':'do_exit'})

    #navigate(turtleBot)

    #rospy.spin()
    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    runTurtleBot()
