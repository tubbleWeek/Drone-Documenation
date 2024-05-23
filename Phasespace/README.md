# Phasespace System

This documentation is for the phasespace system located in Shepherd Labs at the UMN.

## Getting Started

I will have assumed that you have downloaded the Phasesspace master client

To run the master client in Ubuntu you must install it using wine

To install and run:

```
wine msiexec /i whatever-filename.msi 
wine start whatever-filename.msi
```

You can then configure it according to the manual

the IP for the phasespace is `cs.phasespace.cs.umn.edu` or `160.94.220.134`


## Using Phasespace

I have attached a `psnode.cpp` and `listener.cpp` file in this directory.

To use them:

```
rosrun ${package node is located in} psnode cs-phasespace.cs.umn.edu
```

And in another terminal:

```
rosrun ${package node is located in} listener
```

Now if you have configured your master client correctly you should be able to see the positions of the LEDs being trasmitted to your computer

**Please note in my system I have phantom LEDs this is why my listener loops through half of the marker list if your system does not then removethe changes I made**
