`# Apriltags Localization System in Gazebo

_**This assumes you have already set up your drone simulation before hand**_


## Setting up drone model

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

You can either change the line or download the `.sdf` file I have included in this directory
