"""
  basic FFT
"""
import numpy as np 

import matplotlib.pyplot as plt

x = np.zeros(100)
x[0] = 1
a = x
#a = np.sin(x) + np.sin(3*x) + np.sin(50*x) + np.sin(22*x)

b = np.fft.fft(a)


plt.subplot(2, 1, 1)
plt.plot(a)

plt.subplot(2, 1, 2)
plt.plot(b.real)
plt.show()


print b