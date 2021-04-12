# -*- coding: utf-8 -*-
"""
练习5
"""

import numpy           # 全名导入
import numpy.linalg
rr = numpy.array([[50, 0, -30], [0, 65, -15], [-30, -15, 45]])
b = numpy.array([0, 0, 120])
R = [5, 10, 20]
currents = []
for r in R:
    v = rr.copy()
    v[0][0] += r
    v[0][1] -= r
    v[1][0] -= r
    v[1][1] += r
    currents.append(numpy.linalg.solve(v, b))

for r, i in zip(R, currents):
    print("电阻为%d欧姆时的电流为："%(r), i)