# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:39:09 2021

@author: samuel
"""

import matplotlib.pyplot as plt

def logistic_map(n, x0=0.5, r=1.0):
    """构造单峰映射
    
    参数
    ____
    n: int
        数值个数
    x0: float
        序列初始值
    r：float
        r的值
    返回值
    ______
    x[]: float list
        一个单峰映射
    """
    x = [x0]
    for i in range(1, n):
        x.append(r*x[i-1]*(1-x[i-1]))
    return x

# (1)
l1 = logistic_map(2000, r=1.5)
l2 = logistic_map(2000, r=3.5)
fig = plt.figure(figsize=(16, 4))
plt.plot(l1[-100:-1],  c='r', label='r=1.5')
plt.plot(l2[-100:-1],  c='b', label='r=3.5')
plt.xlabel('idx')
plt.ylabel('x')
plt.legend(loc='best')
plt.show()

#(2)
x0 = 0.5
i = 0
m = 1
l = [x0]
r = [m]
while i < 2000:
    l.append(r[-1]*l[-1]*(1-l[-1]))
    if abs(m - 4) <= 1e-2:
        m = 1
    else:
        m += 0.01
    r.append(m)
    i += 1

fig = plt.figure(figsize=(16, 4))
plt.plot(r[-1000:-1], l[-1000:-1], 'k.', c='r')
plt.xlabel('r')
plt.ylabel('x')
plt.show()