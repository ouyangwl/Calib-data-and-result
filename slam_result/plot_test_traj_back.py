#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:18:24 2017

@author: hyj
"""
import os
import numpy as np
import pandas
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rcParams
import seaborn

seaborn.set_style("ticks")
plt.rcParams["font.family"]='Times New Roman'
plt.rcParams["font.size"]=15
np.set_printoptions(suppress = True)

# imu_pose
timestamp1 = []
position_x1 = []
position_y1 = []
position_z1 = []
with open("baby/imu_data.csv", 'r') as fp1:
  csv_result1 = pandas.read_csv(fp1)
  row_list1 = csv_result1.values.tolist()
  for l1 in row_list1:
    timestamp1.append(l1[0])
    position_x1.append(l1[1])
    position_y1.append(l1[2])
    position_z1.append(l1[3])

# mocap_pose
timestamp2 = []
position_x2 = []
position_y2 = []
position_z2 = []
with open("baby/mocap_data.csv", 'r') as fp2:
  csv_result2 = pandas.read_csv(fp2)
  row_list2 = csv_result2.values.tolist()
  for l2 in row_list2:
    timestamp2.append(l2[0])
    position_x2.append(l2[1])
    position_y2.append(l2[2])
    position_z2.append(l2[3])

# camera_pose
position_x3 = []
position_y3 = []
position_z3 = []
with open("baby/camera_data.csv", 'r') as fp3:
  csv_result3 = pandas.read_csv(fp3)
  row_list3 = csv_result3.values.tolist()
  for l3 in row_list3:
    position_x3.append(l3[1])
    position_y3.append(l3[2])
    position_z3.append(l3[3])

# camera_noise_pose
position_x4 = []
position_y4 = []
position_z4 = []
with open("baby/camera_noise_data.csv", 'r') as fp4:
  csv_result4 = pandas.read_csv(fp4)
  row_list4 = csv_result4.values.tolist()
  for l4 in row_list4:
    position_x4.append(l4[1])
    position_y4.append(l4[2])
    position_z4.append(l4[3])

### plot 3d
fig = plt.figure()
# plt.axes(position_x2, position_y2, position_z2, label='mocap')

ax = fig.gca(projection='3d')

# ax.plot(position_x1, position_y1, position_z1, label='gt')
ax.plot(position_x2, position_y2, position_z2, label='mocap')
# ax.plot(position_x3, position_y3, position_z3, label='camera')
# ax.plot(position_x4, position_y4, position_z4, label='camera_noise')
# ax.plot([position_x1[0]], [position_y1[0]], [position_z1[0]], 'r.', label='start')


# ax.legend(fontsize=22)
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.set_xticks(np.arange(-5, 14, 4))
ax.set_yticks(np.arange(0, 11, 3))
ax.set_zticks(np.arange(1, 9, 2))
ax.set_xlim(-2.5,12.5)
ax.set_ylim(0,10)
ax.set_zlim(2,8)
ax.set_xlabel('X (m)', fontsize=15, labelpad=1)
ax.set_ylabel('Y (m)', fontsize=15, labelpad=1)
ax.set_zlabel('Z (m)', fontsize=15, labelpad=1)
# ax.set_xlabel('X', fontsize=20, labelpad=8.5)
# ax.set_ylabel('Y', fontsize=20, labelpad=8.5)
# ax.set_zlabel('Z', fontsize=20, labelpad=8.5)
plt.tick_params(pad=0.1)
# plt.tick_params(bottom=False, top=False, left=False, right=False)
# ax.grid(color='r', linestyle='--', linewidth = 0.5)
# plt.grid(ls = ":",color = "gray",alpha = 0.5)
# ax.tick_params(bottom=False, top=False, left=False, right=False)
# plt.axis('off')

plt.show()


# plt.plot(position_x1, position_y1, c='g', label='gt')
# plt.plot(position_x2, position_y2, c='y', label='mocap')
# plt.plot(position_x3, position_y3, c='r', label='camera')
# plt.plot(position_x4, position_y4, c='b', label='camera_noise')

# plt.xlabel("x-axis (m)")
# plt.ylabel("y-axis (m)")

# plt.legend()
# plt.show()


# fig, ax = plt.subplots(3, 1, figsize=(14,7))

# ax[0].set_xlabel("timestamp")
# ax[0].set_ylabel("rotvel_x")

# ax[1].set_xlabel("timestamp")
# ax[1].set_ylabel("rotvel_y")

# ax[2].set_xlabel("timestamp")
# ax[2].set_ylabel("rotvel_z")
 
# # draw the figure, the color is r = read
# ax[0].plot(timestamp1, position_x1, c='r')
# ax[0].plot(timestamp2, position_x2, c='b')
# ax[0].legend(['spline_velx','trans_velx'])

# ax[1].plot(timestamp1, position_y1, c='r')
# ax[1].plot(timestamp2, position_y2, c='b')
# ax[1].legend(['spline_vely','trans_vely'])

# ax[2].plot(timestamp1, position_z1, c='r')
# ax[2].plot(timestamp2, position_z2, c='b')
# ax[2].legend(['spline_velz','trans_velz'])

# plt.show()