# -*- coding: utf-8 -*-
"""
练习6

求一元二次方程的实数解
"""

import math
import random

def quadratic(a, b, c):
    """求解一元二次方程
    
    参数
    ____
    a: float
        方程二次项系数
    b: float
        方程一次项系数
    c: float
        方程常数项
    返回值
    ______
    x: float tuples
        空，方程无解
        (x1, x2) 方程的两个实数解    
    """
    x1, x2 = None, None
    if a == 0:
        if b == 0:
            if c == 0:
                #print('方程有任意解')
                x1 = random.uniform(0.0, 100.0)
                x2 = random.uniform(0.0, 100.0)
            else:
                #print('方程无解')
                pass
        else:
            x = -c / b
            #print('方程有解：x=%.2f' % x)
            x1 = x
            x2 = x
    else:
        q = b * b - 4 * a * c
        if q > 0:
            x1 = (-b + math.sqrt(q)) / a / 2
            x2 = (-b - math.sqrt(q)) / a / 2
            #print("一元二次方程的解为x1=%.2f，x2=%.2f" % (x1, x2))
        elif q == 0:
            x1 = -b / a / 2
            x2 = x1
            #print("一元二次方程的解相同，x1=x2=%.2f" % (x1))
        else:
            pass
            #print("一元二次方程无解")
    
    if (x1 == None):
        return ()
    else:
        return x1, x2