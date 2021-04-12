# -*- coding: utf-8 -*-
"""
LUdecomp3.py
"""

def LUdecomp3(c,d,e):
    """对形如[c\d\e]的三对角系数矩阵进行LU分解。
    
    参数
    ____
    c: vector
        原始矩阵的c系数向量
    d: vector
        原始矩阵的d系数向量
    e: vector
        原始矩阵的e系数向量
    
    输出
    ____
    c,d,e: 经过LU分解之后的c、d、e系数向量
    """
    n = len(d)
    for k in range(1,n):
        lam = c[k-1]/d[k-1]
        d[k] = d[k] - lam*e[k-1]
        c[k-1] = lam
    return c,d,e

def LUsolve3(c,d,e,b):
    """使用LU法解形如[c\d\e]{x} = {b}的三对角系数矩阵方程。
    
    参数
    ____
    c: vector
        原始矩阵的c系数向量
    d: vector
        原始矩阵的d系数向量
    e: vector
        原始矩阵的e系数向量
    b: vector
        方程的常系数向量
    
    输出
    ____
    b: 原方程的解
    """
    n = len(d)
    for k in range(1,n):
        b[k] = b[k] - c[k-1]*b[k-1]
    b[n-1] = b[n-1]/d[n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - e[k]*b[k+1])/d[k]
    return b