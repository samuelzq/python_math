# -*- coding: utf-8 -*-
"""
练习2

编写一个用来计算三角形面积的函数并验证，假设三角形的三条边的长度分别是a、b和c。
"""

import math

def tri_area(a, b, c):
    """求任意三角形面积
    
    入参
    ____
    a, b, c: float
        分别为三条边的长度
        
    返回值
    ______
    A： float
        A > 0, 三角形面积
        -1, 输入错误
    """
    if (a < 0 or b < 0 or c < 0):
        return -1
    
    if (a > (b + c) or b > (a + c) or c > (a + b)):
        return -1
    
    s = (a + b + c) / 2.0
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return A

def test_A():
    """
    三角形面积函数的测试函数
    """
    a1, b1, c1, s1 = 1, 1, 1, 0.43
    a2, b2, c2, s2 = 3, 4, 5, 6
    a3, b3, c3, s3 = 7, 8, 9, 27
    a4, b4, c4, s4 = 2, -1, 1, -1
    
    
    assert math.isclose(tri_area(a1, b1, c1), s1, rel_tol=0.2), '第一组测试结果错误 %f'%(tri_area(a1, b1, c1))
    assert math.isclose(tri_area(a2, b2, c2), s2, rel_tol=0.2), '第二组测试结果错误 %f'%(tri_area(a2, b2, c2))
    assert math.isclose(tri_area(a3, b3, c3), s3, rel_tol=0.2), '第三组测试结果错误 %f'%(tri_area(a3, b3, c3))
    assert tri_area(a4, b4, c4) == s4, '第四组测试结果错误 %f'%(tri_area(a4, b4, c4))