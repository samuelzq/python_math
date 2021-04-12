# -*- coding: utf-8 -*-
"""
练习3：

梅森质数是形如2^p−1的质数，其中p也是质数。请编写程序找出40以内的所有梅森质数。
"""

import math

def is_prime(n):
    """检测一个整数是否为质数
    
    入参
    ____
    n: int
        待检验整数
        
    返回值
    ______
    p：bool
        True，输入为质数
        False，输入不是质数
    """
    if n <= 1: 
        return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n % i == 0: 
            return False
    return True

p = 2
masson = []
m = math.pow(2, p) - 1
while m < 40:
    if is_prime(m):
        masson.append(m)        
    p += 1
    m = math.pow(2, p) - 1

if masson:
    print("40以内的梅森素数有：")
    for mm in masson:
        print("%d "%(mm), end="")
else:
    print("不存在40以内的梅森素数")