#!/usr/bin/env python

import math
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan


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
        self.l_scan = rospy.Subscriber('/scan', LaserScan, self.lscanCallback)
       # rospy.spin()

        rospy.on_shutdown(self.shutdown)

    def lscanCallback(self, msg):
        output = [msg.ranges[359], msg.ranges[0], msg.ranges[180]]
        rospy.loginfo(output)
        self.scan_output = output

    # move the turtlebot forward at a given speed.
    def moveForward(self, speed):
        move_cmd = Twist()
        move_cmd.linear.x = speed
        self.publisher.publish(move_cmd)

    # turn the turtlebot left.
    def turnLeft(self):
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

    # get distance between the turtlebot and objects surrounding it.
    # return value is in the form: [left, front, right]
    def getObstacles(self):
        scan = rospy.wait_for_message(self.namespace + "/scan", LaserScan)
        return [scan.ranges[719], scan.ranges[0], scan.ranges[360]]

    # stop and shutdown the turtlebot.
    def shutdown(self):
        move_cmd = Twist()
        self.publisher.publish(move_cmd)
        rospy.loginfo("Stopping and shutting down ...")
        exit(0)
