# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 13:00:38 2018

@author: b
"""

import numpy as np

x = np.array([22, 41, 58, 33, 17, 32])
r1 = x > 40
print(r1)

r2 = x[x > 40]
print(r2)

r3 = np.where(x > 40)
print(r3)
