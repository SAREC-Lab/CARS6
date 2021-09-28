#!/usr/bin/env/ python

# Import libraries
import json


# Parse the task planner json file into individual states.
def parse_plan(task_planner_path):
    with open(task_planner_path) as planner_file:
        planner_states = json.load(planner_file)
        parsed_states = []
        counter = 0
        for state in planner_states["states"]:
            state.index = counter
            parsed_states.append(state)
            counter += 1

        return parsed_states
