# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:09:32 2021

@author: samuel
"""

import numbers
import math

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:09:32 2021

@author: samuel
"""

class FixedPoint(numbers.Rational):
    """
    “比例数”。 这些数包括一个整数值和一个比例因子。这种数可以被应用到币值计算。
    例如：对于世界上的多数货币，我们可以使用100为比例因子，并将所有计算都精确到分。
    """
    __slots__ = ( "value", "scale", "default_format" )
    
    def __new__(self, value, scale=100 ):
        self = super(FixedPoint, self).__new__(self)
        if isinstance(value,FixedPoint):
            self.value= value.value
            self.scale= value.scale
        elif isinstance(value,int):
            self.value= value
            self.scale= scale
        elif isinstance(value,float):
            self.value= int(scale*value+.5)
            self.scale= 1
        else:
            raise TypeError
        digits= int(math.log10(scale))
        self.default_format= "{{0:.{digits}f}}".format(digits=digits)
        return self
    
    def __str__(self):
        return self.__format__( self.default_format )
    
    def __repr__(self):
        return "%s(%d, scale=%d)" % (self.__class__.__name__, 
                                     self.value, self.scale )
        
    def __format__( self, specification ):
        if specification == "": 
            specification = self.default_format
        return specification.format( self.value/self.scale )
            
    def numerator(self):
        return self.value
    
    def denominator(self):
        return self.scale
    
    def __add__( self, other ):
        """ 前向加法 """
        if not isinstance(other,FixedPoint):
            new_scale= self.scale
            new_value= self.value + other*self.scale
        else:
            new_scale= max(self.scale, other.scale)
            new_value= (self.value*(new_scale//self.scale)
                        + other.value*(new_scale//other.scale))
        return FixedPoint( int(new_value), scale=new_scale )
    
    def __sub__( self, other ):
        """ 前向减法 """
        if not isinstance(other,FixedPoint):
            new_scale= self.scale
            new_value= self.value - other*self.scale
        else:
            new_scale= max(self.scale, other.scale)
            new_value= (self.value*(new_scale//self.scale)
                        - other.value*(new_scale//other.scale))
        return FixedPoint( int(new_value), scale=new_scale )
    
    def __mul__( self, other ):
        """ 前向乘法 """
        if not isinstance(other,FixedPoint):
            new_scale= self.scale
            new_value= self.value * other
        else:
            new_scale= self.scale * other.scale
            new_value= self.value * other.value
        return FixedPoint( int(new_value), scale=new_scale )
    
    def __truediv__( self, other ):
        """ 前向除法 """
        if not isinstance(other,FixedPoint):
            new_value= int(self.value / other)
        else:
            new_value= int(self.value / (other.value/other.scale))
        return FixedPoint( new_value, scale=self.scale )
    
    def __floordiv__( self, other ):
        """ 前向地板除法 """
        if not isinstance(other,FixedPoint):
            new_value= int(self.value // other)
        else:
            new_value= int(self.value // (other.value/other.scale))
        return FixedPoint( new_value, scale=self.scale )
    
    def __mod__( self, other ):        
        """ 前向取模 """
        if not isinstance(other,FixedPoint):
            new_value= (self.value/self.scale) % other
        else:
            new_value= self.value % (other.value/other.scale)
        return FixedPoint( new_value, scale=self.scale )
    
    def __pow__( self, other ):
        """ 前向幂 """
        if not isinstance(other,FixedPoint):
            new_value= (self.value/self.scale) ** other
        else:
            new_value= (self.value/self.scale) ** (other.value/other.scale)
        return FixedPoint( int(new_value)*self.scale, scale=self.scale )

    
    def __abs__( self ):
        return FixedPoint( abs(self.value), self.scale )
    
    def __float__( self ):
        return self.value/self.scale
    
    def __int__( self ):
        return int(self.value/self.scale)
    
    def __trunc__( self ):
        return FixedPoint( math.trunc(self.value/self.scale), self.scale )
    
    def __ceil__( self ):
        return FixedPoint( math.ceil(self.value/self.scale), self.scale )
    
    def __floor__( self ):
        return FixedPoint( math.floor(self.value/self.scale), self.scale )
    
    def __round__( self, ndigits ):
        return FixedPoint( round(self.value/self.scale, ndigits=0), self.scale )
    
    def __neg__( self ):
        return FixedPoint( -self.value, self.scale )
    
    def __pos__( self ):
        return self
    
    def __radd__( self, other ):
        if not isinstance(other,FixedPoint):
            new_scale= self.scale
            new_value= other*self.scale + self.value
        else:
            new_scale= max(self.scale, other.scale)
            new_value= (other.value*(new_scale//other.scale)
                        + self.value*(new_scale//self.scale))
        return FixedPoint( int(new_value), scale=new_scale )
    
    def __rsub__( self, other ):
        if not isinstance(other,FixedPoint):
            new_scale= self.scale
            new_value= other*self.scale - self.value
        else:
            new_scale= max(self.scale, other.scale)
            new_value= (other.value*(new_scale//other.scale)
                        - self.value*(new_scale//self.scale))
        return FixedPoint( int(new_value), scale=new_scale )
    
    def __rmul__( self, other ):
        if not isinstance(other,FixedPoint):
            new_scale= self.scale
            new_value= other*self.value
        else:
            new_scale= self.scale*other.scale
            new_value= other.value*self.value
        return FixedPoint( int(new_value), scale=new_scale )
    
    def __rtruediv__( self, other ):
        if not isinstance(other,FixedPoint):
            new_value= self.scale*int(other / (self.value/self.scale))
        else:
            new_value= int((other.value/other.scale) / self.value)
        return FixedPoint( new_value, scale=self.scale )
    
    def __rfloordiv__( self, other ):
        if not isinstance(other,FixedPoint):
            new_value= self.scale*int(other // (self.value/self.scale))
        else:
            new_value= int((other.value/other.scale) // self.value)
        return FixedPoint( new_value, scale=self.scale )
    
    def __rmod__( self, other ):
        if not isinstance(other,FixedPoint):
            new_value= other % (self.value/self.scale)
        else:
            new_value= (other.value/other.scale) % (self.value/self.scale)
        return FixedPoint( new_value, scale=self.scale )
    
    def __rpow__( self, other ):
        if not isinstance(other,FixedPoint):
            new_value= other ** (self.value/self.scale)
        else:
            new_value= (other.value/other.scale) ** self.value/self.scale
        return FixedPoint( int(new_value)*self.scale, scale=self.scale )
    
    def __eq__( self, other ):
        if isinstance(other, FixedPoint):
            if self.scale == other.scale:
                return self.value == other.value
            else:
                return self.value*other.scale//self.scale == other.value
        else:
            return abs(self.value/self.scale - float(other)) < .5/self.scale
        
    def __ne__( self, other ):
        return not (self == other)
    
    def __le__( self, other ):
        return self.value/self.scale <= float(other)
    
    def __lt__( self, other ):
        return self.value/self.scale <  float(other)
    
    def __ge__( self, other ):
        return self.value/self.scale >= float(other)
    
    def __gt__( self, other ):
        return self.value/self.scale >  float(other)
    
if __name__ == '__main__':
    f1 = FixedPoint(12.3, 10)
    f2 = FixedPoint(13, 10)
    print(f1, f2)
    print(f1+f2)
    print(repr(f1))