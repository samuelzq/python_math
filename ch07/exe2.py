# -*- coding: utf-8 -*-
"""
求任意多边形的形心
"""

import numpy           # 全名导入

v = numpy.array([[9, 5], [12, 8], [5, 11], [3, 4], [5, 6], [9, 5]])
a = 0
l, w = v.shape
for i in range(l-1):
   a += (numpy.linalg.det(v[i: i+2]))  # 对原数组切片求所得行列式的值
a = abs(a) / 2
print(a)

x = 0
y = 0
for i in range(l-1):
    s = v[i: i+2]
    x += (numpy.linalg.det(s) * s[...,0].sum())   # 公式7-19 Cx
    y += (numpy.linalg.det(s) * s[...,1].sum())   # 公式7-19 Cy
x = x / 6 / a
y = y / 6 / a
print(x, y)