# Intel RealSense for Apriltag Detection

**This will assume that you have already set up your Apriltag detection as described in the Apriltag detection in Gazebo section**

## Downloading the Intel RealSense SDK and ROS nodes

Install the ROS packages as describe in [here](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy)

**Please note this is for ROS1 there is another package that works for ROS2**

**You do not need to create a new workspace, you can just put the files into your existing workspace**

You can test if you downloaded it correctly by running:

```
realsense-viewer
```

If you use a virtual machine you will have to attach the camera to the VM and configure your USB settings

## Configuring .yaml Files for Running Apriltag Detection 

First run the RealSense ROS node with

```
roslaunch realsense2_camera rs_camera.launch
```

and by running 

```
rostopic list
```

we can see the image topics we need the Apriltag node to subscribe too

```
/camera/color/camera_info
/camera/color/image_raw
/camera/color/image_raw/compressed
/camera/color/image_raw/compressed/parameter_descriptions
/camera/color/image_raw/compressed/parameter_updates
/camera/color/image_raw/compressedDepth
/camera/color/image_raw/compressedDepth/parameter_descriptions
/camera/color/image_raw/compressedDepth/parameter_updates
/camera/color/image_raw/theora
/camera/color/image_raw/theora/parameter_descriptions
/camera/color/image_raw/theora/parameter_updates
/camera/color/metadata
/camera/depth/camera_info
/camera/depth/image_rect_raw
/camera/depth/image_rect_raw/compressed
/camera/depth/image_rect_raw/compressed/parameter_descriptions
/camera/depth/image_rect_raw/compressed/parameter_updates
/camera/depth/image_rect_raw/compressedDepth
/camera/depth/image_rect_raw/compressedDepth/parameter_descriptions
/camera/depth/image_rect_raw/compressedDepth/parameter_updates
/camera/depth/image_rect_raw/theora
/camera/depth/image_rect_raw/theora/parameter_descriptions
/camera/depth/image_rect_raw/theora/parameter_updates
/camera/depth/metadata
/camera/extrinsics/depth_to_color
/camera/motion_module/parameter_descriptions
/camera/motion_module/parameter_updates
/camera/realsense2_camera_manager/bond
/camera/rgb_camera/auto_exposure_roi/parameter_descriptions
/camera/rgb_camera/auto_exposure_roi/parameter_updates
/camera/rgb_camera/parameter_descriptions
/camera/rgb_camera/parameter_updates
/camera/stereo_module/auto_exposure_roi/parameter_descriptions
/camera/stereo_module/auto_exposure_roi/parameter_updates
/camera/stereo_module/parameter_descriptions
/camera/stereo_module/parameter_updates
/diagnostics
/rosout
/rosout_agg
/tf
/tf_static
```

The two topics we are interested in are `/camera/color/camera_info` and `/camera/color/image_raw`

Now we need to change the `continuous_detection.launch`

the camera name topic needs to be changed to `/camera/color`

save and exit, then open up `tags.yaml` in your apriltags_ros package

Add the Apriltag that you are going to use into the standalone tags and tag bundles then save and exit

## Running

In one terminal run

```
roslaunch continuous_detection.launch
```

in another 

```
rostopic echo tag_detections
```

Now if you point your RealSense camera at the apriltag you should get the position of the camera with respect to the apriltag

If you want to view the images coming from the realsense run

```
rosrun rviz rviz
```

and add an image that views the image topic of choice

**If you are not getting your positions from the apriltag most likely it is an issue with the configs for apriltag_ros but you can also check the raw image using rviz**
