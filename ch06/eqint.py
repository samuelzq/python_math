# -*- coding: utf-8 -*-
"""
在数学中，假设在一个集合 X上定义一个等价关系（用〜来表示），
则 X中的某个元素 a的等价类就是在 X中等价于 a的所有元素所形成的子集。
例如，如果对于等价关系为在整数集做模7运算，则1与8（15、22、依此类推）属于相同的等价
类，而3与10属于相同的等价类。3〜10表示3和10是属于同一等价类中的两个对象。
现在我们使用等价类的概念来定义整数类型。
"""

class Eqint:    
    """
    使用等价类的概念定义的整数类型。
    0等价为空集；
    1等价于含有一个元素的集合；
    2等价于含有两个元素的集合；
    ……
    n等价于含有n个元素的集合。
    """
    def __init__(self, sequence):
        """
        使用一个序列来初始化对象。
        该序列可以是列表、元组和字符串等可迭代对象。
        """
        self.__s = []
        self.__length = 0
        for i in sequence:
            self.__s.append(i)
            self.__length += 1
    
    def __str__(self):
        return (str(self.__length))
    
    def __repr__(self):
        return str(self.__length)
    
    def __eq__(self, other):
        """
        比较是否相等
        """
        if self.__length != other.__length:
            return False
        else:
            return True
        
    def __add__(self, other):
        """
        前向加法
        """
        return Eqint(self.__s + other.__s)
    
if __name__ == '__main__':
    positive_integers = []
    i = 0
    while i < 10:
        eqn = Eqint(positive_integers)
        positive_integers.append(eqn)
        i += 1
    print(positive_integers)