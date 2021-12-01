#!/usr/bin/env python

# Import libraries
import rospy
from moveturtle import Turtlebot
from maze_navigator import navigate


# Run bot
def runTurtleBot():
    rospy.init_node('squishy_turtlebot3')
    turtleBot = Turtlebot(namespace="squishy")

    navigate(turtleBot)

    rospy.spin()


if __name__ == '__main__':
    runTurtleBot()
