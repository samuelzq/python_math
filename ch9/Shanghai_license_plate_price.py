# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:54:05 2020

@author: samuel
"""

import numpy
import csv
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl

# 读取数据时保留第一行的栏位字段
license_data = numpy.genfromtxt('Shanghai_license_plate_price.csv', delimiter=',', names=True)

# 数据文件中包含的不同数据项
field = ['Total number of license issued', 'lowest price', 'avg price', 'Total number of applicants']

# 用于调整数据标签在的Y坐标，因为部分数据最后一个值可能比较接近
y_offsets = {'Total number of license issued': 0, 'lowest price': 1500,
             'avg price': -1500,
             'Total number of applicants': 0}

# 获取数据最大值
y_max = 0
y_min = numpy.Inf

for column in field:
    if column == 'Date':
        continue
    column_rec_name = column.replace('\n', '_').replace(' ', '_')
    ymax = numpy.amax(license_data[column_rec_name])
    ymin = numpy.amin(license_data[column_rec_name])
    if (y_max < ymax):
        y_max = ymax
    if (y_min > ymin):
        y_min = ymin

# 读取CSV文件中第一列的内容，并将其转换为X日期刻度
with open('Shanghai_license_plate_price.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    column0 = [row[0] for row in reader]

x= []
for t in column0:
    d = time.strptime(t, "%b-%y")      # 将日期字符串转换为时间元组
    # 将日期时间对象转换为Matplotlib日期后，添加到列表x
    x.append(mpl.dates.date2num(datetime.datetime(d.tm_year, d.tm_mon, 1))) 

fig, ax = plt.subplots(1, 1, figsize=(24, 20))

# 不同数据对应的颜色编码
ax.set_prop_cycle(color=['slateblue', 'red', 'blue', 'black'])

# 删除绘图框线。
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 确保轴刻度只显示在绘图的底部和左侧。
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

#fig.subplots_adjust(left=.06, right=.75, bottom=.02, top=.94)

# 根据日期和数值范围设置X、Y显示范围
ax.set_xlim(x[0], x[-1])
ax.set_ylim(y_min, y_max)

# 去除默认刻度线；对于我们刚刚绘制的刻度线，它们是不必要的。
#ax.tick_params(axis='both', which='both', labelsize=14,
#               bottom=False, top=False, labelbottom=True,
#               left=False, right=False, labelleft=True)

for column in field:
    # 把每一条线分别用它自己的颜色画出来。
    column_rec_name = column.replace('\n', '_').replace(' ', '_')
    line, = ax.plot(x, column_rec_name, data=license_data,  lw=1.5)
    
    # 在每行的右端添加一个文本标签。
    y_pos = license_data[column_rec_name][-1]
    y_max = numpy.amax(license_data[column_rec_name])
    d = numpy.where(license_data[column_rec_name] == y_max)
        
    # 添加特定的偏移量，因为一些标签重叠了。
    y_pos += y_offsets[column]

    ax.text(x[-1], y_pos, column, fontsize=14, color=line.get_color())
    for idx in numpy.nditer(d):        
        ax.annotate('{label} max value'.format(label=column_rec_name), 
                     xy = (x[idx], y_max), 
                     xytext = (x[idx]+500, y_max+3500+y_offsets[column]),
                     arrowprops = dict(facecolor = line.get_color(), shrink = 0.05))
    

# X轴刻度以年月的形式显示
monthsLoc = mpl.dates.MonthLocator(interval=6)
monthsLoc1 = mpl.dates.MonthLocator(interval=2)
ax.xaxis.set_major_locator(monthsLoc)
ax.xaxis.set_minor_locator(monthsLoc1)
monthsFmt = mpl.dates.DateFormatter('%Y-%b')
ax.xaxis.set_major_formatter(monthsFmt)
fig.autofmt_xdate(bottom=0.18)
fig.subplots_adjust(left=0.18)
#plt.savefig('Shgh_car_licence_price.png')

# 定义坐标系大小
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005
rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

# 创建正方形绘图
fig = plt.figure(figsize=(16, 16))

# 在绘图上划分坐标系
ax = fig.add_axes(rect_scatter)
ax_histx = fig.add_axes(rect_histx, sharex=ax)
ax_histy = fig.add_axes(rect_histy, sharey=ax)

# 坐标系相邻的区域不显示刻度
ax_histx.tick_params(axis="x", labelbottom=False)
ax_histy.tick_params(axis="y", labelleft=False)

count = license_data.size
avg_mean = int(numpy.mean(license_data['avg_price'])/1000)
avg_median = int(numpy.median(license_data['avg_price'])/1000)
avg_min = int(numpy.min(license_data['avg_price'])/1000)
avg_max = int(numpy.max(license_data['avg_price'])/1000)
avg_25p, avg_50p, avg_75p = (numpy.percentile(
    license_data['lowest_price'], [25, 50, 75])/1000).astype(int)

lowest_mean = int(numpy.mean(license_data['lowest_price'])/1000)
lowest_median = int(numpy.median(license_data['lowest_price'])/1000)
lowest_min = int(numpy.min(license_data['lowest_price'])/1000)
lowest_max = int(numpy.max(license_data['lowest_price'])/1000)
lowest_25p, lowest_50p, lowest_75p = (numpy.percentile(
    license_data['lowest_price'], [25, 50, 75])/1000).astype(int)
corr = numpy.corrcoef(license_data['lowest_price'],
                      license_data['avg_price'])
# 绘图
ax.scatter(license_data['avg_price'], license_data['lowest_price'])
ax.text(20000, 80000, 'PPCs: {}'.format(corr[0][1]), style='italic',
        bbox={'facecolor': 'lightblue', 'alpha': 0.5, 'pad': 10})

ax_histx.hist(license_data['avg_price'], bins=20)
ax_histx.set_title('average price')
text = 'Mean: {}k \nMax: {}k\nMedian: \
       {}k\n25%: {}k\n50%: {}k\n75%: {}k'.format(avg_mean, avg_max, 
                     avg_median, avg_25p, avg_50p, avg_75p)
ax_histx.text(50000, 15, text, style='italic',
        bbox={'facecolor': 'lightblue', 'alpha': 0.5, 'pad': 10})
ax_histy.hist(license_data['lowest_price'],orientation='horizontal')
ax_histy.set_title('lowest price')
text = 'Mean: {}k \nMax: {}k\nMedian: \
       {}k\n25%: {}k\n50%: {}k\n75%: {}k'.format(lowest_mean, lowest_max, 
                     lowest_median, lowest_25p,
                     lowest_50p, lowest_75p)
ax_histy.text(25, 55000, text, style='italic',
        bbox={'facecolor': 'lightblue', 'alpha': 0.5, 'pad': 10})
#plt.savefig('Shgh_car_licence_avg_lowest_correlation.png')

plt.show()