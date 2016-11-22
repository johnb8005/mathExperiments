"""
shows evolution of compounded interest for different period of time and different growth rates
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

f, axarr = plt.subplots(1, 2)

fig = plt.figure()
ax = fig.gca(projection='3d')
n = np.arange(0, 10, .1)
r = np.arange(0, 1, 0.01)
n, r = np.meshgrid(n, r)
z = (1+r)**n
z = np.log(z)
surf = ax.plot_surface(n, r, z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()