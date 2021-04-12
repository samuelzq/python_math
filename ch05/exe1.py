# -*- coding: utf-8 -*-
"""
练习1：
在一个大小为 8×4 的图上绘制函数f(x)=x^2的曲线，x在区间[-3, 3]内取值，颜色是红色，
线的粗细为 2（默认为 1）。

"""

import matplotlib.pyplot as plt

x = [float(i/100) for i in range(-300, 300)]
y = []
for i in x:
    y.append(i**2)

fig = plt.figure(figsize=(8, 4))
plt.plot(x,y, c='red', linewidth=2, label=r'$f(x) = x^2$') # 红色，宽度2
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()