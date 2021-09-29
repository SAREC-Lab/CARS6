#!/usr/bin/env python

# Import libraries
import smach
from states.plan import Plan
from states.circleL import CircleL
from states.circleR import CircleR
from states.stop import Stop


def run_state_machine(pub_init_pose, pub_controls, plan):
    # create state machine
    sm = smach.StateMachine(outcomes=['do_exit'])
    sm.userdata.plan = plan
    sm.userdata.curr_state = {}

    # open the container
    with sm:
        # add states to the container
        smach.StateMachine.add('Plan', Plan(),
                               transitions={
                                   "do_exit": "Stop", "do_circleL": "CircleL", "do_circleR": "CircleR"},
                               remapping={"plan": "plan",
                                          "curr_state": "curr_state"})
        smach.StateMachine.add("CircleL", CircleL(pub_init_pose, pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("CircleR", CircleR(pub_init_pose, pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("Stop", Stop(),
                               transitions={"do_exit": "do_exit"})

    # execute SMACH plan
    outcome = sm.execute()
