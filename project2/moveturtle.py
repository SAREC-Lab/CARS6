import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class Turtlebot():

    def __init__(self, namespace=""):
        self.namespace = namespace
        self.x = 0
        self.y = 0
        self.angle = 0
        self.LIDAR_ERR = 0.05
        self.rate = rospy.Rate(10)

        # Register publishers and subscribers
        self.publisher = rospy.Publisher(self.namespace + '/cmd_vel', Twist, queue_size=1)

        rospy.on_shutdown(self.shutdown)
