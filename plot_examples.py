# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


# Examples 1
plt.clf()

plt.plot([1,2,3,4])
plt.ylabel('Demo for plot')

###############################################

# Examples 2
# plotting another on the same figure

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

###############################################

# Examples 3
# creating a new figure 

plt.clf()
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])

###############################################

import numpy as np

# Examples 4
# creating a new figure

plt.clf()
x = np.arange(1, 11)
y = x ** 2

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y is equal to x squared')
plt.legend(['y = x**2'])