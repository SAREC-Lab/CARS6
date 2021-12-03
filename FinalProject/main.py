#!/usr/bin/env python

# Import libraries
from ChaCha.chacha import Chacha
import rospy
import smach
import time
import json
from plan_parser import parse_plan
from geometry_msgs.msg import Twist
# Add states to library
from ChaCha.forward import Forward
from ChaCha.backward import Backward
from ChaCha.circle import Circle
from ChaCha.clap import Clap
from ChaCha.turnL import TurnL
from ChaCha.turnR import TurnR


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


def runTurtleBot(plan):
    rospy.init_node('squishy_turtlebot3')
    turtleBot = Turtlebot(namespace="squishy")

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['do_exit'])
    sm.userdata.plan = plan
    sm.userdata.plan_length = len(plan)
    sm.userdata.curr_state = {}

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('Plan', Plan(),
                               transitions={'do_forward': 'Forward', 'do_backward': 'Backward', 'do_circle': 'Circle',
                                            'do_turnL': 'TurnL', 'do_turnR': 'TurnR', 'do_clap': 'Clap', 'do_chacha': 'Chacha', 'do_exit': 'Stop'})
        smach.StateMachine.add('Forward', Forward(),
                               transitions={'do_plan': 'Plan'})
        smach.StateMachine.add('Backward', Backward(),
                               transitions={'do_plan': 'Plan'})
        smach.StateMachine.add('Circle', Circle(),
                               transitions={'do_plan': 'Plan'})
        smach.StateMachine.add('TurnL', TurnL(),
                               transitions={'do_plan': 'Plan'})
        smach.StateMachine.add('TurnR', TurnR(),
                               transitions={'do_plan': 'Plan'})
        smach.StateMachine.add('Clap', Clap(),
                               transitions={'do_clap': 'Clap'})
        smach.StateMachine.add('Chacha', Chacha(),
                               transitions={'do_chacha': 'Chacha'})
        smach.StateMachine.add('Stop', Stop(),
                               transitions={'do_exit': 'do_exit'})

    # navigate(turtleBot)

    # rospy.spin()
    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    plan = parse_plan("FinalProject/plans/plan2.json")
    runTurtleBot(plan)
