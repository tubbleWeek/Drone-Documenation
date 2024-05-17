# Apriltags Localization System in Gazebo

_**This assumes you have already set up your drone simulation before hand**_


## Setting up Drone Model

For this I will have my drone's camera face downwards, you can have it face anywhere you would like

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

Now you need to edit the `tags.yaml` file

It can be found in `~/catkin_ws/src/apriltag_ros/apriltag_ros/config`

You need to edit it so it is the exact same at the `tags.yaml` that is posted in this directory

By adding:

```
      {id: 0, size: 1.0, name: tag0}
```

And:

```
     {
       name: 'CUSTOM_BUNDLE_NAME',
       layout:
         [
           {id: 0, size: 1.0, x: 0, y: 0, z: 0, qw: 0, qx: 0, qy: 0, qz: 0}
         ]
     }
```

If it is easier you can just download and replace it

## Running the Detector

1. Start the Drone Simulation
2. Insert the Apriltag model - in the insert tab in Gazebo(It is near the top left of the Gazebo window)
   - Use the one with the end tag `_00000`
3. Using the terminal window where you ran `./start.sh`
   - Set the mode to guided using `mode guided`
   - and launch drone with `arm throttle` and `takeoff 4`
4. Position the tag underneath the drones camera
   - The tag not appear to be present due to being in the ground plane, you can just move the tag up in the Z direction
5. Run continuous_detection using ```roslaunch apriltag_ros continuous_detection.launch```

You can see the results by echoing the `tag_detections` topic using"

```
rostopic echo tag_detections
```

You can also see the view of the camera using RVIZ

Launch RVIZ with:

```
rosrun rviz rviz
```

Add a image using the add button and then open the dropdown menu for the image and select the image stream that you wish to view

## Accessing The Data

To access the data held in the `/tag_detections` topic first you need to see the structure of the topic

You ucan do this by running:

```
rosmsg show rosmsg show apriltag_ros/AprilTagDetectionArray 
```

It should show:

```
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
apriltag_ros/AprilTagDetection[] detections
  int32[] id
  float64[] size
  geometry_msgs/PoseWithCovarianceStamped pose
    std_msgs/Header header
      uint32 seq
      time stamp
      string frame_id
    geometry_msgs/PoseWithCovariance pose
      geometry_msgs/Pose pose
        geometry_msgs/Point position
          float64 x
          float64 y
          float64 z
        geometry_msgs/Quaternion orientation
          float64 x
          float64 y
          float64 z
          float64 w
      float64[36] covariance
```

By this heirarchy structure we can see that the position is located in `detection.pose.pose.pose.position`

I have written a simple subsciber node for ROS you can find it in this directory

