# -*- coding: utf-8 -*-
"""
求出由（1，1）、（3，1）、（2，3）确定的三角形的形心，并将其绘制出来
"""

import matplotlib.pyplot as plt
import numpy           # 全名导入

tri = numpy.array([[1, 1], [3, 1], [2, 3]])
centroid = tri.mean(axis = 0)                        # 按列求平均
trishape = plt.Polygon(tri, ec='r', alpha=0.2, lw=5) # 创建三角形对象
_, ax = plt.subplots(figsize=(4, 4))
ax.add_patch(trishape)
ax.set_ylim([.5, 3.5])
ax.set_xlim([.5, 3.5])
ax.scatter(*centroid, color='g', marker='D', s=70)
ax.scatter(*tri.T, color='b',  s=70)
plt.show()