# Drone Simulation in Gazebo

## Setup for Enviroment

If you do not have github installed run:

```
sudo apt install git
```

**Optional:** install TMUX

```
sudo apt install tmux
```

TMUX is a tool that allows you to have multiple terminals in the same window

For help with the commands you can visit [Tmux Cheat Sheet](https://tmuxcheatsheet.com/)

### Installing ArudPilot

I will be using ArduPilot in this project, there are other flight controllers such as PX4 that you can use

**To Install**

Navigate to your root folder 'cd ~' and run:

```
git clone https://github.com/ArduPilot/ardupilot.git
```

This will pull all the relevant files from ArduPilots github directory

Now navigate inside the arudpilot directory on your computer

```
cd ardupilot
```

And install its dependecies

```
Tools/environment_install/install-prereqs-ubuntu.sh -y
```

After this is completed reload ArduPilot's profile using:

```
. ~/.profile
```

I will be using the Copter module in ArduPilot:

```
git checkout Copter-4.0.4
git config --global url.https://.insteadOf git://
git submodule update --init --recursive
```

To check if the intallation was successful:

Run:

```
cd ~/ardupilot/ArduCopter
sim_vehicle.py -w
```

Now we will need to compile the code in ArduPilot

Run:
```
cd ~/ardupilot
./waf configure
make waf build
```

_Disclaimer: This may take awhile_




