#! /usr/bin/python3
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class turtle:
    def __init__(self):
        self.pose = Pose()
        self.pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=1)
        self.sub_1 = rospy.Subscriber('turtle2/pose', Pose, self.key_pose)
        self.sub_2 = rospy.Subscriber('turtle1/pose', Pose, self.follow_pose)

    def follow_pose(self, turtlePos):
        msg = Twist()
        rotate = math.atan2(turtlePos.y - self.pose.y, turtlePos.x - self.pose.x)
        msg.angular.z = rotate - self.pose.theta
        msg.linear.x = turtlePos.linear_velocity
        self.pub.publish(msg)

    def key_pose(self, turtlePos):
        self.pose = turtlePos

rospy.init_node('following_turtle')
following_turtle = turtle()
rospy.spin()
