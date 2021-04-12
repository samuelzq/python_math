# -*- coding: utf-8 -*-
"""
练习3

编写一个函数计算物体从高度H（单位：米）处下落所需要的时间t。并用以下数据验证。
（1） H = 1m（t≈0.452s）。
（2） H = 10m（t≈1.428s）。
（3） H = 0m（t = 0s）。
（4） H = -1m（请思考合理的解）。

"""

import math
from scipy.constants import g as const_g

def falling_time(h):
    """获取物体自由落体的时间
    
    参数
    ____
    h: float
        物体开始自由落体时的高度
    
    返回值
    ______
    t: float
        >= 0, 物体自由落体时间
        -1, 输入值错误
    """
    if (h < 0):
        return -1
    
    return math.sqrt(h*2/const_g)

def test_ftime():
    """
    测试函数
    """
    h1, t1 = 1, 0.452
    h2, t2 = 10, 1.428
    h3, t3 = 0, 0
    h4, t4 = -1, -1
    
    
    assert math.isclose(falling_time(h1), t1, rel_tol=0.2), '第一组测试结果错误 %f'%(falling_time(h1))
    assert math.isclose(falling_time(h2), t2, rel_tol=0.2),  '第二组测试结果错误 %f'%(falling_time(h2))
    assert math.isclose(falling_time(h3), t3, rel_tol=0.2),  '第三组测试结果错误 %f'%(falling_time(h3))
    assert falling_time(h4) == t4,  '第四组测试结果错误 %f'%(falling_time(h4))