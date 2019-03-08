# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plt.clf()

# create a numpy array 
x = np.linspace(-100, 100, 21)
# create y array as a function of x
y = (x + 1) * (x - 1)  

# plot large blue dots, connected by dotted lines
plt.plot(x, y, 'bo:') 
plt.xlabel('x')
plt.ylabel('y')
plt.title('parabola')
plt.grid()   
plt.savefig('fig-parabola.jpg')

