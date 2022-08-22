#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class Listener():
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('exemplo', Twist, self.callback)
        self.pub1 = rospy.Publisher('result1', Float32, queue_size=10)
        self.pub2 = rospy.Publisher('result2', Float32, queue_size=10)

    def callback(self, msg):
        lf = Float32()
        af = Float32()

        lx, ly, lz = msg.linear.x, msg.linear.y, msg.linear.z
        ax, ay, az = msg.angular.x, msg.angular.y, msg.angular.z

        lmod = (lx**2 + ly**2 + lz**2)**(1/2)
        amod = (ax**2 + ay**2 + az**2)**(1/2)

        lf.data = lmod
        af.data = amod

        rospy.loginfo(lf)
        rospy.loginfo(af)

        self.pub1.publish(af)
        self.pub2.publish(lf)

if __name__ == '__main__':
    l = Listener()
    rospy.spin()