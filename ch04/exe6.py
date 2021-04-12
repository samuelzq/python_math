# -*- coding: utf-8 -*-
"""
练习6：

完美数是一种特殊的自然数。它的所有的真因数的和恰好等于它本身。
编写程序找到10000之内所有的完美数。

"""

from exe5 import defactor

perfect = []

for i in range(1, 10000):
    f = defactor(i)
    if i == sum(f):
        perfect.append(i)

print("10000以内的完美数有：")
for i in perfect:
    print(i, end=" ")