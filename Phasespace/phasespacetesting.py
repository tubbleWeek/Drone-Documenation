import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import rosbag
import rospy
import sys

if(len(sys.argv) != 3):
    print("Usage: testrosbag.py $\{apriltag_detections\} $\{phasespace_markers\}")
    sys.exit(-1)

apriltag_detections = sys.argv[1]
phasespace_markers = sys.argv[2]


zlist = []
time = []

bag = rosbag.Bag(apriltag_detections)#Open the rosbag

for topic, msg, t in bag.read_messages(topics=['/tag_detections']):
    if(msg.detections != []):
        tempz = msg.detections[0].pose.pose.pose.position.z
        zlist.append(tempz/10)
        time.append(rospy.Time.to_sec(t))

bag.close()

time = np.array(time)
zlist = np.array(zlist)
plt.plot(time, zlist, label = "Apriltag Reading")


bag = rosbag.Bag(phasespace_markers)

dists = []
time = []
for topic, msg, t in bag.read_messages(topics=['/phasespace_markers']):
    dronePoint = np.array((msg.markers[11].x, msg.markers[11].y, msg.markers[11].z))
    apriltagPoint = np.array((msg.markers[6].x, msg.markers[6].y, msg.markers[6].z))
    dist = np.linalg.norm(dronePoint - apriltagPoint)/1000
    dists.append(dist)
    time.append(rospy.Time.to_sec(t))
bag.close()

dists = np.array(dists)
time = np.array(time)
plt.plot(time, dists, label = "Euclidian Distance")



plt.legend()

#Display the final plot
plt.show()

#finished


