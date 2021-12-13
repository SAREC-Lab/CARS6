#!/usr/bin/env python

# Import libraries
import rospy
import smach
import time
import pathlib
import websocket
import thread
import time
from plan_handler import get_filtered_plans
from geometry_msgs.msg import Twist
from plan_parser import parse_plan
from ChaChaDance.plan import Plan
from ChaChaDance.stop import Stop
from ChaChaDance.forward import Forward
from ChaChaDance.backward import Backward
from ChaChaDance.turnL import TurnL
from ChaChaDance.turnR import TurnR
from ChaChaDance.circle import Circle

handling_msg = False

def on_message(ws, message):
    global handling_msg

    if handling_msg:
        return

    handling_msg = True

    plan = get_filtered_plans(message)
    if plan:
        runTurtleBot(plan)

    handling_msg = False


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        time.sleep(1)
        print("WSS connection opened")
    thread.start_new_thread(run, ())


def runTurtleBot(plan):
    pub_controls = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['do_exit'])
    sm.userdata.plan = plan
    sm.userdata.plan_length = len(plan)
    sm.userdata.curr_state = {}

    with sm:
        # Add states to the container
        smach.StateMachine.add('Plan', Plan(),
                                transitions={'do_forward': 'Forward', 'do_backward': 'Backward',
                                             'do_turnL': 'TurnL', 'do_turnR': 'TurnR', 'do_exit': 'Stop',
                                             'do_circle': 'Circle'})
        smach.StateMachine.add('Forward', Forward(pub_controls),
                                transitions={'do_plan': 'Plan'},
                                remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("Backward", Backward(pub_controls),
                                transitions={"do_plan": "Plan"},
                                remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("TurnL", TurnL(pub_controls),
                                transitions={"do_plan": "Plan"},
                                remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("TurnR", TurnR(pub_controls),
                                transitions={"do_plan": "Plan"},
                                remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("Circle", Circle(pub_controls),
                                transitions={"do_plan": "Plan"},
                                remapping={"curr_state": "curr_state"})
        smach.StateMachine.add("Stop", Stop(pub_controls),
                                transitions={"do_exit": "do_exit"})
        outcome = sm.execute()


def read_cha_cha():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://squushy.herokuapp.com",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()


if __name__ == '__main__':
    rospy.init_node('squishy_turtlebot3')

    abs_path = pathlib.Path(__file__).parent.resolve()
    plan_path = str(abs_path) + "/plans/plan1.json"
    plan = parse_plan(plan_path)
    print(plan)

    read_cha_cha()
    #runTurtleBot(plan)
