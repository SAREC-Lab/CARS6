#!/usr/bin/env/ python

import rospy
import smach
import time
from geometry_msgs.msg import Twist
# TO DO: import each state and command 






# define state Stop
class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['do_exit'])
        self.counter = 0

    def execute(self, userdata):
	time.sleep(1)
        return 'do_exit'
      
# Main
def main():

    rospy.init_node('smach_turtle_dance')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['do_exit'])

    # Open the container
    with sm:
        # Add states to the container
	smach.StateMachine.add('Plan', Plan(), 
                               transitions={'do_forward':'Forward', 'do_backward': 'Backward', 'do_circleL':'CircleL', 'do_circleR': 'CirlceR', 
					    'do_turnL':'TurnL', 'do_turnR':'TurnR', 'do_threepoint': 'ThreePoint', 'do_exit':'Stop'})
        smach.StateMachine.add('Forward', Forward(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('Backward', Backward(), 
                                transitions={'do_plan':'Plan'})
        smach.StateMachine.add('CircleL', CircleL(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('CircleR', CircleR(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('TurnL', TurnL(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('TurnR', TurnR(), 
                               transitions={'do_plan':'Plan'}) 
        smach.StateMachine.add('ThreePoint', ThreePoint(), 
                               transitions={'do_plan':'Plan'})
        smach.StateMachine.add('Stop', Stop(), 
                               transitions={'do_exit':'do_exit'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
