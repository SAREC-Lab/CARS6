#!/usr/bin/env python

import math
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from tf.transformations import euler_from_quaternion


class Turtlebot():

    def __init__(self, namespace=""):
        self.namespace = namespace
        self.x = 0
        self.y = 0
        self.angle = 0
        self.scan_output = []
        self.LIDAR_ERR = 0.05
        self.rate = rospy.Rate(10)

        # Register publishers and subscribers
        self.publisher = rospy.Publisher(
            self.namespace + '/cmd_vel', Twist, queue_size=1)
        self.sub_odom = rospy.Subscriber(
            self.namespace + '/odom', Odometry, self.odometryCallback)
        self.laser_scanner = rospy.Subscriber(
            '/scan', LaserScan, self.laserScannerCallback)

        rospy.on_shutdown(self.shutdown)

    # odometry callback function.
    def odometryCallback(self, odometry):
        _, _, yaw = euler_from_quaternion(
            [odometry.pose.pose.orientation.x, odometry.pose.pose.orientation.y,
             odometry.pose.pose.orientation.z, odometry.pose.pose.orientation.w])
        self.angle = (round(math.degrees(yaw)) + 180) % 360
        self.x = round(odometry.pose.pose.position.x, 3)
        self.y = round(odometry.pose.pose.position.y, 3)

    # laser scanner callback function.
    def laserScannerCallback(self, msg):
        output = [msg.ranges[359], msg.ranges[0], msg.ranges[180]]
        # rospy.loginfo(output)
        self.scan_output = output

    # get distance between the turtlebot and objects surrounding it.
    # return value is in the form: [left, front, right]
    def getObstacles(self):
        return self.scan_output

    # move the turtlebot forward at a given speed.
    def moveForward(self, speed):
        move_cmd = Twist()
        move_cmd.linear.x = speed
        self.publisher.publish(move_cmd)

    # turn the turtlebot left.
    def turnLeft(self):
        rospy.loginfo("Attempting to run turnLeft")
        move_cmd = Twist()
        turn_angle = 90
        move_cmd.angular.z = math.radians(turn_angle / 4)
        while (turn_angle % 360) > self.angle and not rospy.is_shutdown():
            self.publisher.publish(move_cmd)
            self.rate.sleep()

        move_cmd = Twist()
        self.publisher.publish(move_cmd)

    # turn the turtlebot right.
    def turnRight(self):
        move_cmd = Twist()
        turn_angle = 90
        move_cmd.angular.z = -math.radians(turn_angle / 4)
        start_angle = self.angle
        final_angle = ((start_angle - turn_angle) + 360) % 360
        while self.angle > 0 and self.angle < final_angle and not rospy.is_shutdown():
            self.publisher.publish(move_cmd)
            self.rate.sleep()
        while self.angle > final_angle and not rospy.is_shutdown():
            self.publisher.publish(move_cmd)
            self.rate.sleep()

        move_cmd = Twist()
        self.publisher.publish(move_cmd)

    # stop and shutdown the turtlebot.
    def shutdown(self):
        move_cmd = Twist()
        self.publisher.publish(move_cmd)
        rospy.loginfo("Stopping and shutting down ...")
        exit(0)
