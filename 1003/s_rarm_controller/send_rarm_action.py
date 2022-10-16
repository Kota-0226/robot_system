#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, actionlib, sys, time

from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectoryPoint

def main():
    print("Initializing node... ")
    rospy.init_node("joint_trajectory_client_example")
    rospy.sleep(1)
    print("Running. Ctrl-c to quit")
    positions = { 'RARM_JOINT0': 0.0, 'RARM_JOINT1': 0.0, 'RARM_JOINT2':-1.6,
                  'RARM_JOINT3': 0.0, 'RARM_JOINT4': 0.0, 'RARM_JOINT5': 0.0, }
    client = actionlib.SimpleActionClient( # SimpleActionClient オブジェクト
        '/rarm_controller/follow_joint_trajectory_action', FollowJointTrajectoryAction)
    if not client.wait_for_server(timeout=rospy.Duration(10)): # ActionServer が反応しない
        sys.exit(1)
        # init goal
    goal = FollowJointTrajectoryGoal() # ActionGoal オブジェクト
    goal.goal_time_tolerance = rospy.Time(1) # 終了条件を設定
    goal.trajectory.joint_names = positions.keys() # 指示する関節名
    # 1st point
    point = JointTrajectoryPoint()
    point.positions = positions.values() # 指示する関節角度
    point.time_from_start = rospy.Duration(3) # 到達時刻
    goal.trajectory.points.append(point)
    # 2nd points
    point = JointTrajectoryPoint()
    positions['RARM_JOINT1'] = -0.7; positions['RARM_JOINT2'] = -2.3 # 指示する関節角度を修正
    point.positions = positions.values() # 指令値に関節角度を指定
    point.time_from_start = rospy.Duration(6) # 到達時刻
    goal.trajectory.points.append(point)
    # 3rd points
    point = JointTrajectoryPoint()
    positions['RARM_JOINT1'] = 0 ; positions['RARM_JOINT2'] = -1.6 # 指示する関節角度を修正
    point.positions = positions.values() # 指令値に関節角度を指定
    point.time_from_start = rospy.Duration(9) # 到達時
    goal.trajectory.points.append(point)
    # send goal
    goal.trajectory.header.stamp = rospy.Time.now()
    client.send_goal(goal) # ActionGoal を送出
    print(goal)
    print("waiting...")
    if not client.wait_for_result(timeout=rospy.Duration(20)): # 最大 20 秒結果を待つ
            rospy.logerr("Timed out waiting for JTA")
    rospy.loginfo("Exitting...")

if __name__ == "__main__":
    main() 
