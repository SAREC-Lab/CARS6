#!/usr/bin/env/ python

# Import libraries
import rospy
from geometry_msgs.msg import Twist
from moves import move_circle, move_forward, move_left, move_right
from datetime import timedelta, datetime

# Global Counters
in_progress = False
last_moves = []
last_move_time = datetime.utcnow() - timedelta(days=1)

# Return plans depending on song filter
def get_filtered_plans(last_words):
    last_words = ' '.join(last_words.split()[-5:])

    global in_progress
    global last_move_time

    if in_progress:
        return []

    in_progress = True

    last_words_str = str(last_words)
    last_words_lower = last_words_str.lower()

    #print(last_words_lower)
    cur_time = datetime.utcnow()

    pub_controls = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    if cur_time > last_move_time + timedelta(seconds=2.5):
        cha_cha_handler(last_words_lower, pub_controls)
        clap_handler(last_words_lower, pub_controls)
        left_handler(last_words_lower, pub_controls)
        back_handler(last_words_lower, pub_controls)
        one_hop_handler(last_words_lower, pub_controls)
        right_foot_handler(last_words_lower, pub_controls)
        left_foot_handler(last_words_lower, pub_controls)
        circle_handler(last_words_lower, pub_controls)

    in_progress = False

    return []


def cha_cha_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 1 and \
            last_moves[-1] == 'cha cha':
                return []

    matches = [
        "we're gonna get funky",
        "we're going to get funky",
        "cha-cha",
        "cha cha",
        "time to get funky"
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('cha cha')

            print("Found cha-cha move. Attempting to execute.")

            move_circle(pub_controls, 1)
            move_circle(pub_controls, -1)

            return True

    return False


def clap_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 2 and \
            last_moves[-1] == 'clap':
                return []

    matches = [
        "everybody clap your hands",
        "clap clap clap"
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('clap')

            print("Found clap. Attempting to execute.")

            move_forward(pub_controls, 1)
            move_forward(pub_controls, -1)

            return True

    return False


def left_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 1 and \
            last_moves[-1] == 'left':
                return []

    matches = [
        "to the left",
        "turn the lamp"
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('left')

            print("Found left. Attempting to execute.")

            move_left(pub_controls)

            return True

    return False


def back_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 1 and \
            last_moves[-1] == 'back':
                return []

    matches = [
        "take it back",
        "back now y'all"
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('back')

            print("Found back. Attempting to execute.")

            move_forward(pub_controls, -1)

            return True

    return False

def one_hop_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 1 and \
            last_moves[-1] == 'one hop':
                return []

    matches = [
        "one hop this time",
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('one hop')

            print("Found one hop. Attempting to execute.")

            move_forward(pub_controls, -1)

            return True

    return False

def right_foot_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 1 and \
            last_moves[-1] == 'right foot':
                return []

    matches = [
        "right foot",
        "to the right now",
        "the right now",
        "right now"
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('right foot')

            print("Found right foot. Attempting to execute.")

            move_right(pub_controls)

            return True

    return False

def left_foot_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 1 and \
            last_moves[-1] == 'left foot stomp':
                return []

    matches = [
        "left foot",
        "left foot let's stomp",
        "left foot lets stomp"
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('left foot stomp')

            print("Found left foot. Attempting to execute.")

            move_left(pub_controls)

            return True

    return False

def circle_handler(last_words, pub_controls):
    global last_moves
    global last_move_time

    if len(last_moves) >= 1 and \
            last_moves[-1] == 'circle':
                return []

    matches = [
        "turn it out",
        "turn it up"
    ]

    for match in matches:
        if match in last_words:
            last_move_time = datetime.utcnow()
            last_moves.append('circle')

            print("Found circle. Attempting to execute.")

            move_circle(pub_controls, 1)

            return True

    return False
