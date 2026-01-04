# import necessary module
import pandas
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.collections import LineCollection
import csv
import numpy as np
from matplotlib import rcParams
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


plt.rcParams["font.family"] = "Times New Roman"


#获取数据
traj_gt = np.load('paper_result/6traj_mycalib.npy')
#将数据分段
xs = [[x1, x2] for x1, x2 in zip(traj_gt[:-1,0], traj_gt[1:,0])]
ys = [[x1, x2] for x1, x2 in zip(traj_gt[:-1,1], traj_gt[1:,1])]
segs_2d = [list(zip(x, y)) for x, y in zip(xs, ys)]

#读取误差文件
error_mycalib = np.load('paper_result/6error_mycalib.npy')
error_kalibr = np.load('paper_result/6error_kalibr.npy')


#colorbar的最大最小值设为两组误差的最大最小值
min_map = min(np.min(error_mycalib), np.min(error_kalibr))
max_map = max(np.max(error_mycalib), np.max(error_kalibr))
cmap=plt.get_cmap('jet')
norm = mpl.colors.Normalize(vmin=min_map, vmax=max_map, clip=True)

#进行误差到colorbar的映射
mapper_mycalib = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
mapper_mycalib.set_array(error_mycalib)
colors_mycalib = [mapper_mycalib.to_rgba(a) for a in error_mycalib]
line_collection_mycalib = LineCollection(segs_2d, colors=colors_mycalib, linewidths=2, linestyles="solid")

mapper_kalibr = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
mapper_kalibr.set_array(error_kalibr)
colors_kalibr = [mapper_kalibr.to_rgba(a) for a in error_kalibr]
line_collection_kalibr = LineCollection(segs_2d, colors=colors_kalibr, linewidths=2, linestyles="solid")

#进行画图
fig, axes = plt.subplots(1, 2, figsize=(12,7))
fig.subplots_adjust(left=0.073, bottom=0.09, right=0.90, top=0.94)
for ax in axes.flat:
  ax.set_xlabel("x (m)", fontsize=20, labelpad=1)
  ax.set_ylabel("y (m)", fontsize=20, labelpad=1)
  ax.tick_params(axis='x', labelsize=18)
  ax.tick_params(axis='y', labelsize=18)
  ax.set_xticks([-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
  # ax.set_xlim(np.min(traj_gt[:,0])-0.1, np.max(traj_gt[:,0])+0.1)
  # ax.set_ylim(np.min(traj_gt[:,1])-0.1, np.max(traj_gt[:,1])+0.1)
  ax.set_xlim(-0.5,1)
  ax.set_ylim(-1.8,-0.3)


axes[0].add_collection(line_collection_mycalib)
axes[0].set_title("APE(m) of the proposed method", fontsize=20, pad=10)
axes[1].add_collection(line_collection_kalibr)
axes[1].set_title("APE(m) of Kalibr method", fontsize=20, pad=10)

#绘制colorbar（两个图共用）
axpos = axes[1].get_position()
caxpos = mpl.transforms.Bbox.from_extents(axpos.x1+0.02, axpos.y0, axpos.x1+0.04, axpos.y1)
cax = axes[1].figure.add_axes(caxpos)
cbar = fig.colorbar(mapper_mycalib, ticks=[min_map, (max_map-(max_map-min_map)/2), max_map], cax=cax)
cbar.ax.set_yticklabels(["{0:0.3f}".format(min_map),
                         "{0:0.3f}".format(max_map - (max_map - min_map) / 2),
                         "{0:0.3f}".format(max_map)], fontsize=18)
plt.show()

