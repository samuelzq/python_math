# -*- coding: utf-8 -*-
"""
练习5：

请编写程序输出一个整数n的所有真因数（即除了自身以外的约数）。
"""

def defactor(n):
    """计算整数n所有真因数之和
    
    参数
    ____
    n: int
        待分解的整数
    
    返回值
    ______
    factor: int list
        真因数列表      
    """
    df = []
    for i in range(1, n//2+1):
        if n % i == 0:
            df.append(i)
    return df

def test_dfactor():
    # 测试函数
    n1, f1 = 12, [1, 2, 3, 4, 6]
    n2, f2 = 31, [1]
    assert f1 == defactor(n1), '第一组测试结果错误 {}'.format(defactor(n1))
    assert f2 == defactor(n2), '第一组测试结果错误 {}'.format(defactor(n2))
    

if __name__ == '__main__':
    n = int(input('请输入一个整数: '))
    f = defactor(n)
    
    for i in f:
        print(i, ' ', end="")