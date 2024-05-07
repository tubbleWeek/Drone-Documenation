# Drone Simulation in Gazebo

## Setup for Environment

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

**Optional:** install HELIX

HELIX is a text editor, you can use any other editor that fits your preference such as vim

```
snap install helix --classic
```


## Installing ArudPilot

I will be using ArduPilot in this project, there are other flight controllers such as PX4 that you can use

**To Install**

Navigate to your root folder 'cd ~' and run:

```
git clone https://github.com/ArduPilot/ardupilot.git
```

This will pull all the relevant files from ArduPilot's github directory

Now navigate inside the arudpilot directory on your computer

```
cd ardupilot
```

And install its dependencies

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

To check if the installation was successful:

Run:

```
cd ~/ardupilot/ArduCopter
sim_vehicle.py -w
```

This will launch a SITL simulation, you can stop it using `ctrl + c` in the terminal


Now we will need to compile the code in ArduPilot

Run:
```
cd ~/ardupilot
./waf configure
make waf build
```

_Disclaimer: This may take awhile_

### Installing Gazebo

Source gazebo by running in your root terminal:

```
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt update
```

Install gazebo with:

```
sudo apt-get install gazebo11 libgazebo11-dev
```

### Installing ArduPilot Plugins For Gazebo

Run in your root directory:

```
git clone https://github.com/khancyr/ardupilot_gazebo.git
cd ardupilot_gazebo
```

Then build:

```
mkdir build
cd build
cmake ..
make -j4
sudo make install
```

Add source to bash:

```
echo 'source /usr/share/gazebo/setup.sh' >> ~/.bashrc
```

Add the models to gazebo's models:

```
echo 'export GAZEBO_MODEL_PATH=~/ardupilot_gazebo/models' >> ~/.bashrc
. ~/.bashrc
```

### Running Gazebo Simulation

I will use TMUX here but you can just open a new terminal window 

Open TMUX using:

```
tmux
```

&uarr



