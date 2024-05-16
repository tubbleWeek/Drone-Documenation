`# Apriltags Localization System in Gazebo

_**This assumes you have already set up your drone simulation before hand**_


## Setting up Drone Model

For this I will have my drone's camera face downwards, you can have it face anywhere youu would like

In your drones `.sdf` file. _If you are using the IQ api then it can be found in `~/catkin_ws/src/iq_sim/models/drone_with_camera`_

I only changed one line:

```
<pose>0 0 0.15 0 0 0</pose>
```

To

```
<pose>0 0 0.15 0 1.5 0</pose>
```

You can either change the line or download the model folder I have included in this directory

## Getting Apriltags Localization System

To get Apriltags run in a terminal window:

```
cd ~/catkin_ws/src                    
git clone https://github.com/AprilRobotics/apriltag.git     
git clone https://github.com/AprilRobotics/apriltag_ros.git 
cd ~/catkin_ws                          
rosdep install --from-paths src --ignore-src -r -y  
catkin buildNow 
```

Now we need Apriltags models for Gazebo

To get models:

```
git clone https://github.com/koide3/gazebo_apriltag.git
cp -R gazebo_apriltag/models/* ~/.gazebo/models/
```

If you launch your Gazebo simulation you should be able to see the apriltags models in your models selection

## Configuring Apriltags yaml files

While your drone simulation is running in another termianl run:

```
rostopic list
```

From there you should see under what name your camera is publishing its images

If you followed the Drone Simulation setup it should be publishing under the name `webcam`

Now we need to edit the `continuous_detection.launch`

It can be found in `~/catkin_ws/src/apriltag_ros/launch`

You will need to change lines 6 & 7

From:

```
  <arg name="camera_name" default="/camera_rect" />
  <arg name="image_topic" default="image_rect" />
```

To:

```
  <arg name="camera_name" default="/webcam" />
  <arg name="image_topic" default="image_raw" />
```

Then save and close this file



