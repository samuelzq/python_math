# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:38:17 2021

@author: samuel
"""

import numpy
import matplotlib.pyplot as plt

xs = numpy.array([-1.0, -0.5, 0., 0.5, 1.])
ys = numpy.array([-1.0, -0.55, 0., 0.45, 1.])

A =  numpy.vstack([xs, numpy.ones(len(xs))]).T
a1, a0 = numpy.linalg.lstsq(A, ys, rcond=None)[0]
plt.grid(True)
plt.plot(xs, ys, 'o', label='Original data')
plt.plot(xs, a1*xs + a0, 'k', label='Fitted line')
plt.legend()
plt.show()