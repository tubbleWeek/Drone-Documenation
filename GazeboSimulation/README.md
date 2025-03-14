## Drone Simulation in Gazebo

### Prerequisites
1. Ubuntu/Linux **20.04**

**It is important to use `ROS 1` the distribution used will be noetic**
<br />
<br />
<br />
### Guide to Setting Up Environment

If you do not have ROS noetic here is a quick guide:
- You can find the official installation guide on [ROS Wiki Installation Guide](https://wiki.ros.org/noetic/Installation/Ubuntu)

Steps:

Add the installation keys for ROS
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

If you don't have CURL:

```
sudo apt install curl
```

Then to Install:

```
sudo apt update
sudo apt install ros-noetic-desktop-full
```

_I install `ros-noetic-desktop-full` because it contains many tools that can be used, there are other lighter versions that you can install instead_
<br />
<br />
If you use:

**Bash**

In your root `~` folder run:

```
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

**zzh**

In your root `~` folder run:

```
echo "source /opt/ros/noetic/setup.zsh" >> ~/.zshrc
source ~/.zshrc
```

_This lets the OS know where your ROS package is located so you can run ROS-related commands_
<br />
<br />
Then install ROS development tools:

```
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```

Then initialize the tools using:

```
sudo apt install python3-rosdep
```

Followed with:

```
sudo rosdep init
rosdep update
```
<br />
<br />

I will use catkin for most of this project

To get catkin:

```
sudo apt-get update
sudo apt-get install python3-catkin-tools
```
<br />
<br />
To create your first catkin workspace:

```
cd ~
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin init
```
_The name `catkin_ws` is just common convention you can name it whatever you want_

