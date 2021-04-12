# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:21:06 2021

@author: samuel
"""

import math

def factor(n):
    """分解质因数
    
    参数
    ____
    n: int
        待分解的整数
    
    返回值
    ______
    factor: int list
        质因数列表    
    """
    m = []
    while n!=1:    # n==1时，已分解到最后一个质因数
        for i in range(2, int(math.sqrt(n)) + 1):
            while n % i == 0:
                m.append(i)
                n = n/i
        if n!=1:
            m.append(n)
            break
    return m

def test_factor():
    # 测试函数
    n1, f1 = 24, [2, 2, 2, 3]
    n2, f2 = 31, [31]
    assert f1 == factor(n1), '第一组测试结果错误 {}'.format(factor(n1))
    assert f2 == factor(n2), '第一组测试结果错误 {}'.format(factor(n2))

if __name__ == '__main__':
    n = int(input('请输入一个整数: '))
    f = factor(n)

    if f:
        fs = []
        for i in f:
            fs.append(str(i))
        print(n, '=', '×'.join(fs))
    else:
        print(n, "是一个质数")