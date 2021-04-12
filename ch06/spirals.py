# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:05:42 2021

@author: samuel
"""

import math
import matplotlib.pyplot as plt

class Spiral:
    """
    螺线
    
    ...
    属性
    ____
    theta: float
        弧度
    radii: float
        极径
        
    方法
    ____
    draw:
        绘制螺线
    """
    
    def __init__(self):
        self.theta = []
        self.radii = []
        
    def draw(self):
        # 创建极坐标
        ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
        plt.plot(self.theta, self.radii)
        
        # 将默认的角度转换为弧度制
        plt.thetagrids([0, 45, 90, 135, 180, 225, 270, 315], ['0', 'π/4', 'π/2', '3π/4', 'π', '5π/4', '3π/2', '7π/4'])
        plt.show()

# 以下为不同的螺线类型
class Archimedes(Spiral):
    """ 阿基米德螺线 """
    
    def __init__(self, a, b):
        super(Archimedes, self).__init__()
        self.a = a
        self.b = b
        self.f()
        
    def f(self):
        """
        使用以下方程求轴长和转角
        r = aθ + b (a≠0)
        """
        N = 200
        i = 0
        while (i < N):
            t = i * 4 * math.pi / N
            self.theta.append(t)
            self.radii.append(self.a + self.b*t)
            i += 1


class Log(Spiral):
    """ 对数螺线 """
    
    def __init__(self, a, b):
        super(Log, self).__init__()
        self.a = a
        self.b = b
        self.f()
        
    def f(self):        
        """
        使用以下方程求轴长和转角
        r = ae^(bθ)
        """
        N = 800
        i = 0
        while (i < N):
            t = i * 10 * math.pi / N
            self.theta.append(t)
            self.radii.append(self.a * (math.e ** (self.b*t)))
            i += 1

class Hyperbolic(Spiral):
    """ 双曲螺线 """
    
    def __init__(self, a):
        super(Hyperbolic, self).__init__()
        self.a = a
        self.f()
    
    def f(self): 
        """
        使用以下方程求轴长和转角
        r = a/θ
        """
        N = 50
        i = 1
        while (i < N):
            t = i *  math.pi / 10
            self.theta.append(t)
            self.radii.append(self.a /t)
            i += 1

class Fermat(Spiral):
    """ 费马螺线 """
    
    def __init__(self, a):
        super(Fermat, self).__init__()
        self.a = a
        self.f()
    
    def f(self): 
        """
        使用以下方程求轴长和转角
        r = asqrt(θ)
        """
        N = 500
        i = 0
        
        while (i < N):
            t = i *  math.pi / 50
            self.theta.append(t)
            self.radii.append(self.a * math.sqrt(t))
            i += 1


if __name__ == '__main__':
    a = Archimedes(10, 5)
    a.draw()
    l = Log(20, 0.1)
    l.draw()
    h = Hyperbolic(1)
    h.draw()
    f = Fermat(10)
    f.draw()