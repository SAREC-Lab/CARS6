#!/usr/bin/env python

# Import libraries
import rospy
from moveturtle import Turtlebot


# Run bot to solve the maze.
def runTurtleBot():
    rospy.init_node('turtlebot3_maze')

    while not rospy.is_shutdown():
    #     pass
        turtleBot = Turtlebot(namespace="squishy")

        rospy.loginfo("Testing turn")
   # turtleBot.turnLeft()

        #obstacles = turtleBot.scan_output
        rospy.loginfo("Testing obstacles")

    rospy.spin()

if __name__ == '__main__':
    runTurtleBot()
