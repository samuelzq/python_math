# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
import csv
import prettytable as pt
import matplotlib.pyplot as plt

class MyStats():
    """
    用来处理来自国家统计局（https://data.stats.gov.cn/）的统计数据的基类。
    国家统计局的数据格式通常如下：
        
        第1行：  数据库：年度数据
        第2行：  时间：最近xx年
        第3行：  指标，年份1，年份2，……，年份n
        第4行：  指标1
        ……
        第n行：  指标n
        第n+1行：数据来源：国家统计局

    本基类提取不同数据文件对象的公共部分。

    属性
    ----
    file_name: string
        数据文件的文件名。

    raw_data : string list
        以文本形式保存的原始数据。
    
    stats： float list
        统计数据组成的数组。
        
    x： int list
        绘图时，X坐标刻度。

    方法
    ----
    print_data()
        以格式化的方式输出统计数据
    plot_date()
        绘制统计曲线.

    """
    def __init__(self, file_name):
        """
        MyStats类构造函数

        入参
        _____
        file_name: string
           数据文件名

        返回值
        ______
            无
        """
        self.__file_name = file_name
        raw_data = []
        with open(file_name, 'r') as csv_file:
            lines = csv.reader(csv_file)
            for line in lines:
                raw_data.append(line)

        # 将年份提取出来
        import re
        dat_re = re.compile(r'\d+\.?\d*')
        x = [int(dat_re.search(i).group()) for i in raw_data[2] if dat_re.search(i)]

        # 提取统计数据。由于统计是依时间逆序排列，因此需要反转排列顺序。
        self.__stats = numpy.genfromtxt(file_name, delimiter=',',
                                 skip_header=3, skip_footer=1)[..., -1:0:-1]
        self.__raw_data = raw_data
        self.__x = x[-1::-1]

    def __del__(self):
        """
        MyStats类析构函数。
        """
        del self.__raw_data
        del self.__x

    def print_data(self):
        """
        将统计数据格式化输出。
        """
        f_name = True
        tb = pt.PrettyTable()
        for line in self.__raw_data:
            if (len(line) > 1):
                if (f_name == True):
                    tb.field_names = line
                    f_name = False
                else:
                    tb.add_row(line)
            else:
                print(line[0])
        print(tb)

    def plot_date(self, field_names):
        """
        绘制统计图表。
        """
        plt.rcParams['font.sans-serif'] = ['SimHei']

        x_major_locator=plt.MultipleLocator(1)
        ax=plt.gca()
        ax.xaxis.set_major_locator(x_major_locator)

        for i in range(numpy.shape(self.__stats)[0]):
            plt.plot(self.__x, self.__stats[i], marker='.', label=field_names[i])
        plt.legend(loc='upper left')
        plt.show()            

class Population(MyStats):
    label_names = [u'年底总人口', u'男性人口', u'女性人口', u'城镇人口', u'乡村人口']
    
    def __init__(self, file_name):
        super(Population, self).__init__(file_name)
    
    def plot_date(self):        
        plt.xlabel("年份")
        plt.ylabel("人口(万人)")
        super(Population, self).plot_date(self.label_names)

class GDP(MyStats):
    label_names = [u'国内生产总值', u'国内生产总值增长率', u'人均国内生产总值', u'人均国内生产总值增长率']
    
    def __init__(self, file_name):
        super(GDP, self).__init__(file_name)
    
    def plot_date(self):        
        plt.xlabel("年份")
        plt.ylabel("GDP")
        super(GDP, self).plot_date(self.label_names)
    
if __name__ == '__main__':   
    p = GDP('china_gdp.csv')
    p.print_data()
    p.plot_date()
    del p