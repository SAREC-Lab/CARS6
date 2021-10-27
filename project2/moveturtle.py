import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Turtlebot():

    def __init__(self, namespace=""):
