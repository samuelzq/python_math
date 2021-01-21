# -*- coding: utf-8 -*-
"""
indentation.py
本示例文件中含有一处TabError语法错误

"""

def foo():
	for i in range(10):
		print(i)
	print('done')   # 此处缩进使用了tab键
    print('error')

foo()