# ROS Raspberry Pi

## Description:

Raspberry Pi Remotely Operated Robot Car

L298N DC Motor Chip driving Two DC Motors  

Ultrasonic Sensor for Collision avoidance

Python code on ROS

## How to use: 
Must have a second computer with ROS installed (I'm using Ubuntu and ROS Iron)

Source ros setup.bash (/opt/ros/iron/setup.bash)

Must have Raspberry Pi on the same network - don't forget to also match the ROS_DOMAIN_ID (export ROS_DOMAIN_ID=###)

SSH into your Raspberry Pi on 2 separate terminals. 

 o Launch wheelie.py on one
   
 o Launch sensor.py on the other
   
On your ROS-enabled computer, launch the controller node: 

 o For Xbox controller-enabled driving: 
  
		ros2 run joy joy_node
    
 o For keyboard enabled driving: 
  
		ros2 run teleop_twist_keyboard teleop_twist_keyboard
    
