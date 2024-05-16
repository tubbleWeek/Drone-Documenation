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
catkin build
```

Now we need Apriltags models for Gazebo

To get models:

```
git clone https://github.com/koide3/gazebo_apriltag.git
cp -R gazebo_apriltag/models/* ~/.gazebo/models/
```

If you launch your Gazebo simulation you should be able to see the apriltags models in your models selection

## Configuring Apriltags yaml files

