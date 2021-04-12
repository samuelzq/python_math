# -*- coding: utf-8 -*-
"""
LUdecomp5.py
"""

def LUdecomp5(d,e,f):
    """对形如[f\e\d\e\f]的5对角系数矩阵进行LU分解。
    
    参数
    ____
    d: vector
        原始矩阵的d系数向量
    e: vector
        原始矩阵的e系数向量
    f: vector
        原始矩阵的f系数向量
    
    输出
    ____
    d,e,f: 经过LU分解之后的d、e、f系数向量
    """
    n = len(d)
    for k in range(n-2):
        lam = e[k]/d[k]
        d[k+1] = d[k+1] - lam*e[k]
        e[k+1] = e[k+1] - lam*f[k]
        e[k] = lam
        lam = f[k]/d[k]
        d[k+2] = d[k+2] - lam*f[k]
        f[k] = lam
    lam = e[n-2]/d[n-2]
    d[n-1] = d[n-1] - lam*e[n-2]
    e[n-2] = lam
    return d,e,f

def LUsolve5(d,e,f,b):
    """使用LU法解形如[f\e\d\e\f]{x} = {b}的5对角系数矩阵方程。
    
    参数
    ____
    d: vector
        原始矩阵的d系数向量
    e: vector
        原始矩阵的e系数向量
    f: vector
        原始矩阵的f系数向量
    b: vector
        方程的常系数向量
    
    输出
    ____
    b: 原方程的解
    """
    n = len(d)
    b[1] = b[1] - e[0]*b[0]
    for k in range(2,n):
        b[k] = b[k] - e[k-1]*b[k-1] - f[k-2]*b[k-2]
    b[n-1] = b[n-1]/d[n-1]
    b[n-2] = b[n-2]/d[n-2] - e[n-2]*b[n-1]
    for k in range(n-3,-1,-1):
        b[k] = b[k]/d[k] - e[k]*b[k+1] - f[k]*b[k+2]
    return b