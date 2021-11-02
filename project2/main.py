#!/usr/bin/env python

# Import libraries
import rospy
from moveturtle import Turtlebot


# Run bot to solve the maze.
def runTurtleBot():
    rospy.init_node('squishy_turtlebot3')
    turtleBot = Turtlebot(namespace="squishy")

    while not rospy.is_shutdown():
        obstacles = turtleBot.getObstacles()
        rospy.loginfo("Testing obstacles: {}".format(obstacles))

        rospy.loginfo("Testing turn")
        turtleBot.turnLeft()

    rospy.spin()


if __name__ == '__main__':
    runTurtleBot()
