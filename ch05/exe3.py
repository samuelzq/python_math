# -*- coding: utf-8 -*-
"""
练习3：

假设我们扔出去一个球，它的飞行距离由初速度和抛射的角度决定。
假设球从水平地面抛出，请绘制该球在不同仰角和初速度下的运动轨迹。
"""

import math
import matplotlib.pyplot as plt

def fly_time(theata, u = 90):
    """计算球飞行的时间
    
    参数
    ____
    theata: float
        球被抛出时的仰角
    u: float
        球初速度，默认值90米每秒
        
    返回值
    ______
    time: float
        球飞行的时间
    """
    r = math.radians(theata)              # 角度转弧度
    return round(2*u*math.sin(r)/9.8, 3) # 保留3位小数

def get_track(theata, u=90):
    """获取小球飞行轨迹
    
    参数
    ____
    theata: float
        球被抛出时的仰角
    u: float
        球初速度，默认值90米每秒
        
    返回值
    ______
    x[]: float list
        球飞行的水平位置
    y[]: float list
        球飞行的垂直高度
    """
    time = fly_time(theata)
    r = math.radians(theata)
    vx = u*math.cos(r)   # 平速度
    vy = u*math.sin(r)   # 垂直初速度

    x, y = [], []
    t = 0
    while t < time:
        x.append(t*vx)
        y.append(vy*t-9.8*math.pow(t, 2)/2)
        t += 0.001
    return x, y

theata1 = 45   # 抛射角45°
theata2 = 60   # 抛射角60°
theata3 = 30   # 抛射角30°

x1, y1 = get_track(theata1)
x2, y2 = get_track(theata2)
x3, y3 = get_track(theata3)
    
plt.rcParams['font.sans-serif'] = ['SimHei'] # 将字体替换为黑体）
fig = plt.figure(figsize=(8, 4))
plt.plot(x1, y1, c='k', ls='-.', label='u=90, theata=45')
plt.plot(x2, y2, c='b', ls='--', label='u=90, theata=60')
plt.plot(x3, y3, c='r', label='u=90, theata=30')
plt.legend(loc='best')

plt.xlabel('水平距离（单位：米）')
plt.ylabel('上升高度（单位：米）')
plt.title("球的抛射轨迹")
plt.show()