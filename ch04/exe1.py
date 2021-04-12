# -*- coding: utf-8 -*-
"""
练习1
编写用来筛选质数的程序，并将100以内所有质数筛选出来。
"""

d = [i for i in range(100)]
i = 2
j = 1

# 埃拉托斯特尼筛法
while i < 99:
    a = d[i]
    if a == 0:
        i += 1
        continue
    j = i+1
    while j < 100:
        if d[j] != 0 and d[j] % a == 0:
            d[j] = 0
        j += 1
    i += 1

print("100 以内的质数有：")
for i in d[2:]:
    if i != 0:
        print("%d "%(i),end="")