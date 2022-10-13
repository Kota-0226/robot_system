#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy, actionlib
from move_base_msgs.msg import *
if __name__ == '__main__':
    try:
        rospy.init_node('send_goal', anonymous=True)
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        client.wait_for_server() # ActionLib のサーバと通信が接続されることを確認
        goal = MoveBaseGoal()
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.pose.position.x=34;
        goal.target_pose.pose.position.y=32;
        goal.target_pose.pose.orientation.w = 1
        rospy.loginfo("send goal")
        rospy.loginfo(goal)
        client.send_goal(goal) # 目標位置姿勢を goal として送信
        rospy.loginfo("wait for goal ...")
        ret = client.wait_for_result() # ロボットが目標位置姿勢に到達するまで待つ
        rospy.loginfo("done")
    except rospy.ROSInterruptException: pass
