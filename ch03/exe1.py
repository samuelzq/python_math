# -*- coding: utf-8 -*-
"""
练习1

编写一个用来计算长方体体积的函数，假设长方体的长、宽和高分别是a、b和c。
并使用以下值验证函数是否正确。
（1） a=1，b=1，c=1。
（2） a=1，b=2，c=3.5。
（3） a=0，b=1，c=1。
（4） a=2，b=-1，c=1。
"""

def cubic_volume(a, b, c):
    """计算长方体的体积
    
    参数
    ____
    a: float
        长
    b: float
        宽
    c: float
        高
    
    返回值
    ______
    v：float
        v > 0, 体积
        -1, 错误
    """
    if (a < 0 or b < 0 or c < 0):
        return None
    return a * b * c

def test_volume():
    """体积函数的测试函数
   
    参数
    ----
        无    
   
    返回值
    -----
        无
    """
    a1, b1, c1, v1 = 1, 1, 1, 1
    a2, b2, c2, v2 = 1, 2, 3.5, 7
    a3, b3, c3, v3 = 0, 1, 1, 0
    a4, b4, c4, v4 = 2, -1, 1, -1
    
    
    assert cubic_volume(a1, b1, c1)==v1, '第一组测试结果错误 %f'%(cubic_volume(a1, b1, c1))
    assert cubic_volume(a2, b2, c2)==v2, '第二组测试结果错误 %f'%(cubic_volume(a2, b2, c2))
    assert cubic_volume(a3, b3, c3)==v3, '第三组测试结果错误 %f'%(cubic_volume(a3, b3, c3))
    assert cubic_volume(a4, b4, c4)==v4, '第四组测试结果错误 %f'%(cubic_volume(a4, b4, c4))