# Import libraries
import rospy
from moveturtle import Turtlebot


# Run bot to solve the maze.
def runTurtleBot():
    rospy.init_node('turtlebot3_maze')

    # while not rospy.is_shutdown():
    #     pass
    turtleBot = Turtlebot(namespace="squishy")
    rospy.loginfo("Testing turn")
    turtleBot.turnLeft()

    obstacles = turtleBot.getObstacles()
    rospy.loginfo("Testing obstacles {}".format(obstacles))


if __name__ == '__main__':
    runTurtleBot()
