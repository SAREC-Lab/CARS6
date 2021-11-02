#!/usr/bin/env python

import rospy


# navigate the maze.
def navigate(turtleBot):
    rospy.loginfo("attempting to navigate the maze")
    while not rospy.is_shutdown():
        obstacles = turtleBot.getObstacles()
        if len(obstacles) != 3:
            continue

        distLeft, distFront, distRight = obstacles[0], obstacles[1], obstacles[2]
        maxDistance = max(distFront, distLeft, distRight)

        rospy.loginfo("distances: {}".format(obstacles))

        if distFront >= maxDistance:
            turtleBot.moveForward()
        elif distLeft >= maxDistance:
            turtleBot.turnLeft()
        else:
            turtleBot.turnRight()
