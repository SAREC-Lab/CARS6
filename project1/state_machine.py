#!/usr/bin/env python

# Import libraries
import smach
from states.plan import Plan
from states.circleL import CircleL
from states.circleR import CircleR
from states.turnL import TurnL
from states.turnR import TurnR
from states.forward import Forward
from states.backward import Backward
from states.stop import Stop


def run_state_machine(pub_init_pos, pub_controls, plan):
    # create state machine
    sm = smach.StateMachine(outcomes=['do_exit'])
    sm.userdata.plan = plan
    sm.userdata.plan_length = len(plan)
    sm.userdata.curr_state = {}

    # open the container
    with sm:
        # add states to the container
        smach.StateMachine.add('Plan', Plan(pub_init_pos),
                               transitions={
                                   "do_exit": "Stop", "do_circleL": "CircleL", "do_circleR": "CircleR",
                                   "do_turnL": "TurnL", "do_turnR": "TurnR", "do_forward": "Forward", "do_backward": "Backward"},
                               remapping={"plan": "plan", "curr_state": "curr_state", "plan_length": "plan_length"})
        smach.StateMachine.add("CircleL", CircleL( pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("CircleR", CircleR(pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("TurnL", TurnL(pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("TurnR", TurnR(pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("Forward", Forward(pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("Backward", Backward(pub_controls),
                               transitions={"do_plan": "Plan"},
                               remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("Stop", Stop(pub_controls),
                               transitions={"do_exit": "do_exit"})

    # execute SMACH plan
    outcome = sm.execute()
