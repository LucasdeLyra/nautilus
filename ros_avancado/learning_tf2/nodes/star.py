#!/usr/bin/env python3
import rospy

# Because of transformations
import tf_conversions

import tf2_ros
import geometry_msgs.msg
import turtlesim.msg
import math


def solar_system(planet_radii, satellite_radii, star_name, planet_name, satellite_name, x):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    t.header.stamp = rospy.Time.now()
    t.header.frame_id = star_name
    t.child_frame_id = planet_name

    t.transform.translation.x = planet_radii*math.sin(x)
    t.transform.translation.y = planet_radii*math.cos(x)
    t.transform.translation.z = 0.0

    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    t.transform.rotation.w = 1


    j = geometry_msgs.msg.TransformStamped()
    j.header.stamp = rospy.Time.now()
    j.header.frame_id = planet_name
    j.child_frame_id = satellite_name

    j.transform.translation.x = satellite_radii*math.sin(x)
    j.transform.translation.y = satellite_radii*math.cos(x)
    j.transform.translation.z = 0.0

    j.transform.rotation.x = 0
    j.transform.rotation.y = 0
    j.transform.rotation.z = 0
    j.transform.rotation.w = 1

    br.sendTransform(j)
    br.sendTransform(t)
    rate.sleep()

if __name__ == '__main__':
    rospy.init_node('star_position')
    rate = rospy.Rate(108)

    while not rospy.is_shutdown():
        planet_radii = rospy.get_param("/planet/radii")
        satellite_radii = rospy.get_param("/satellite/radii")
        planet_name = rospy.get_param("/planet/name")
        satellite_name = rospy.get_param("/satellite/name")
        t = rospy.Time.now().to_sec()
        solar_system(planet_radii, satellite_radii, "Sun", planet_name, satellite_name, t)