#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import random

class Talker:
    def __init__(self):
        rospy.init_node('talker', anonymous=True)
        self.pub = rospy.Publisher('exemplo', Twist, queue_size=10)
        self.list = list(range(10))
    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            tw = Twist()
            tw.linear.x = random.choice(self.list) 
            tw.linear.y = random.choice(self.list) 
            tw.linear.z = random.choice(self.list)
            tw.angular.x = random.choice(self.list) 
            tw.angular.y = random.choice(self.list) 
            tw.angular.z = random.choice(self.list)
            rospy.loginfo(tw)
            self.pub.publish(tw)
            rate.sleep()


if __name__ == '__main__':
    try:
        t = Talker()
        t.start()
    except rospy.ROSInterruptException:
        pass    