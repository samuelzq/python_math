# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:01:45 2020

@author: samuel
"""

import numpy
import csv
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections

data = numpy.genfromtxt('weatherdata-3111216.csv',
                         delimiter=',', skip_header=1)

with open('weatherdata-3111216.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)

    column = []
    date = []                    # 记录数据中的年月
    year = {}                    # 记录数据中的年
    for row in reader:
        column.append(row['Date'])
        dtime = time.strptime(row['Date'], "%m/%d/%Y")
        date.append((dtime.tm_year, dtime.tm_mon))
        year[dtime.tm_year] = year.get(dtime.tm_year, 0) + 1

# 将年份提取出来
years = list(year.keys())

# 将每月的天数提取出来
h = collections.Counter(date)
days = list(h.values())

precipitation = data[:, -4]       # 日降雨量
rainfall =  numpy.empty((36, 12)) # 月平均降雨量数组

# 计算每月平均
start = 0
stop = 0
it = numpy.nditer(rainfall, op_flags=['readwrite'])

with it:
    i = 0
    start = 0
    stop = 0
    for x in it:
        if (i < len(days)):
            stop += days [i]
            avr = numpy.sum(precipitation[start:stop])
            x[...] = avr
            start = stop
            i += 1
        else:
            x[...] = 0

plt.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(1, 1, figsize=(12, 9))
ax.plot(years, rainfall[:,0])
ax.set_xlabel('年')
ax.set_ylabel('一月份降水量')
plt.show()

mean_rainfall_in_month = rainfall.mean(axis=0)
mean_rainfall_per_year = rainfall.mean(axis=1)
fig, ax = plt.subplots(1, 1, figsize=(12, 9))
ax.plot(years, mean_rainfall_per_year)
ax.set_xlabel('年')
ax.set_ylabel('年均降水量')
plt.show()

std_rainfall_per_year = rainfall.std(axis=1)
fig, ax = plt.subplots(1, 1, figsize=(12, 9))
ax.errorbar(years, mean_rainfall_per_year, yerr = std_rainfall_per_year)
ax.set_xlabel('年')
ax.set_ylabel('年均降水量')
plt.show()

fig, ax = plt.subplots(1, 1, figsize=(12, 9))
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.boxplot(rainfall, labels=months)
ax.set_xlabel('月')
ax.set_ylabel('月降水量')
