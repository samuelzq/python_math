# -*- coding: utf-8 -*-
"""
练习2：

一些人曾认为对于所有质数p， 2^p−1也是质数。请编写程序找到第一个反例。
"""

import math

def get_frac(n):
    """查找一个整数的最小因数
    
    入参
    ____
    n: int
        待检验整数
        
    返回值
    ______
    f: int
        n的最小因数
    """
    
    for i in range(2, int(math.sqrt(n)) + 1): 
        f = n % i
        if  f == 0: 
            return i
    return 1
 
def isPrime(n):
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

found = False
p = 2
while not found:
    if isPrime(p):
        masson = math.pow(2, p) - 1
        if not isPrime(masson):
            f = get_frac(masson)
            print("找到一个反例 p=%d， masson: %d = %d * %d" % (p, masson, f, masson/f))
            found = True
    p += 1    