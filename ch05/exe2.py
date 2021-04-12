# -*- coding: utf-8 -*-
"""
练习2：

在一个大小为 8×4 的图上绘制函数f(x)=sin^2⁡(x-2) e^(-x^2 )的曲线，
x在区间[0, 2]内取值，颜色是黑色，线的粗细为 2（默认为 1）
"""

import math
import matplotlib.pyplot as plt
 
x = [float(i/100) for i in range(0, 200)]
y = []
for i in x:
    y.append(math.pow(math.sin(i-2), 2)*math.exp(-1*math.pow(i,2)))

fig = plt.figure(figsize=(8, 4))
plt.plot(x, y, c='k', linewidth=2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'$f(x)=sin^2(x-2)e^{-x^2}$')
plt.show()