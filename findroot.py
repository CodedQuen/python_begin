import numpy as np
import scipy as sp
import scipy.optimize as opt
import matplotlib.pyplot as plt


f = lambda x: np.cos(x) - x

x = np.linspace(-5, 5, 1000)
y = f(x)
plt.plot(x, y)
plt.axhline(0, color='k')
plt.xlim(-5,5)
plt.show()
