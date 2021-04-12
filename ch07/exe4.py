# -*- coding: utf-8 -*-
"""
带松弛参数的Gauss-Seidel迭代
"""

import numpy as np
import math

def gauss_seidel_omega(a, b, x0, iters=1000, tol = 1.0e-9):
    '''
    带松弛系数的Gauss_Seidel 迭代

    参数
    ____
    a: float Matrix
        系数矩阵
    b: float vector
        常数向量
    x0：float vector
        解的初始值
    iters: int
        迭代次数，默认1000次

    返回值
    ______
    x：float vector
        解向量
    '''
    omega = 1
    k=10
    p=1
    
    m, n = a.shape
    x = x0
    if m != n:
        raise ValueError("输入必须是方阵！")

    for i in range(iters):
        x_i_old = x.copy()
        for i in range(n):
            sum_new = (a[i, : i] * x[: i]).sum()
            sum_old = (a[i, i + 1 :] * x[i + 1 :]).sum()
            x[i] = omega / a[i, i] * (b[i] - sum_new - sum_old) + (1 - omega) * x[i]
        
        # 计算偏差值
        dx = math.sqrt(np.dot(x-x_i_old, x-x_i_old))
        if dx < tol:
            return x, i, omega
        
        # 在k+p次迭代之后，计算松弛系数
        if i == k:
            dx1 = dx
        if i == k+p:
            dx2 = dx
            omega = 2.0/(1.0 + math.sqrt(1.0  \
                                         - (dx2/dx1)**(1.0/p)))
    print('Gauss-Seidel failed to converge')


ITERATION_LIMIT = 1000
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0., 3., -1., 8.]])

b = np.array([6., 25., -11., 15.])

x = np.zeros_like(b)

x, i, w = gauss_seidel_omega(A, b, x0=x, iters=ITERATION_LIMIT)

print("方程组的解: {0}".format(x))
error = np.dot(A, x) - b
print("误差: {0}".format(error))