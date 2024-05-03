## Drone Simulation in Gazebo

### Prerequisites
1. Ubuntu/Linux **20.04**

**It is important to use `ROS 1` most distributions of `ROS 1` will be compatible**

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

Then Install:

```
sudo apt update
sudo apt install ros-noetic-desktop-full
```

_I install `ros-noetic-desktop-full` because it contains many tools that can be used there are other lighter versions_

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
