# import necessary module
import pandas
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import csv
import numpy as np

# load data from file
time1 = []
position_x1 = []
position_y1 = []
position_z1 = []
file_path1 = "lab5_mycalib/traj_estimate.txt"
csv_result1 = pandas.read_csv(file_path1, sep=' ', skiprows=1)
row_list1 = csv_result1.values.tolist()
for l1 in row_list1:
  time1.append((l1[0]))
  position_x1.append(l1[1])
  position_y1.append(l1[2])
  position_z1.append(l1[3])

time2 = []
position_x2 = []
position_y2 = []
position_z2 = []
file_path2 = "lab5_kalibr/traj_estimate.txt"
csv_result2 = pandas.read_csv(file_path2, sep=' ', skiprows=1)
row_list2 = csv_result2.values.tolist()
for l2 in row_list2:
  time2.append((l2[0]))
  position_x2.append(l2[1])
  position_y2.append(l2[2])
  position_z2.append(l2[3])

time3 = []
position_x3 = []
position_y3 = []
position_z3 = []
file_path3 = "lab5_onlinecalib/traj_estimate.txt"
csv_result3 = pandas.read_csv(file_path3, sep=' ', skiprows=1)
row_list3 = csv_result3.values.tolist()
for l3 in row_list3:
  time3.append((l3[0]))
  position_x3.append(l3[1])
  position_y3.append(l3[2])
  position_z3.append(l3[3])


# new a figure and set it into 3d
# fig = plt.figure()
# ax = fig.gca(projection='3d')
 
# # set figure information
# ax.set_title("3D_Curve")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
 
# # draw the figure, the color is r = read
# figure1 = ax.plot(position_x1, position_y1, position_z1, c='r', lw = 2)
# figure2 = ax.plot(position_x2, position_y2, position_z2, c='b')

# plt.show()

plt.plot(position_x1, position_y1, c='r', label='mycalib')
plt.plot(position_x2, position_y2, c='b', label='kalibr')
plt.plot(position_x3, position_y3, c='g', label='onlinecalib')

plt.xlabel("x-axis (m)")
plt.ylabel("y-axis (m)")

plt.legend()
plt.show()


plt.plot(time1, position_z1, c='r', label='mycalib')
plt.plot(time2, position_z2, c='b', label='kalibr')
plt.plot(time3, position_z3, c='g', label='onlinecalib')

plt.xlabel("timestamp (s)")
plt.ylabel("z-axis (m)")

plt.legend()
plt.show()

