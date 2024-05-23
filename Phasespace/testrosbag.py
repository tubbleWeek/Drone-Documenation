import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import rosbag
import rospy

fig, axs = plt.subplots(2, 4)

xlist = []
ylist = []
zlist = []
time = []
bag = rosbag.Bag('posesv2.bag')

for i in range(0,8):
    temp_xlist = []
    temp_ylist = []
    temp_zlist = []
    temp_time = []
    for topic, msg, t in bag.read_messages(topics=['/phasespace_markers']):
        temp_time.append(rospy.Time.to_sec(t))
        temp_xlist.append(msg.markers[i].x)
        temp_ylist.append(msg.markers[i].y)
        temp_zlist.append(msg.markers[i].z)
    xlist.append(temp_xlist)
    ylist.append(temp_ylist)
    zlist.append(temp_zlist)    
    time.append(temp_time)


bag.close()
for i in range (0,8):
    xlist[i] = np.array(xlist[i])
    ylist[i] = np.array(ylist[i])
    zlist[i] = np.array(zlist[i])
    time[i] = np.array(time[i])
j = 0
for i in range (0,8):
    if i == 4:
        j += 1
    axs[j,i%4].plot(time[i], xlist[i], label = "x position")
    axs[j,i%4].plot(time[i], ylist[i], label = "y position")
    axs[j,i%4].plot(time[i], zlist[i], label = "z position")
    axs[j,i%4].set_title(f'LED {i}')

for ax in axs.flat:
    ax.set(xlabel='Time(seconds)', ylabel='Position(cm)')

for ax in axs.flat:
    ax.label_outer()

plt.legend()

plt.show()


