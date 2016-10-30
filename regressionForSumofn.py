# usage of regressions to find coefficients of formula to sum terms `i^m` from 0 to n
import numpy as np
from numpy.linalg import inv

def plot(y,z):
  import matplotlib.pyplot as plt

  plt.plot(y, '.')
  plt.plot(z)
  plt.show()

# solve Ordinary Least Squares
def solveOLS(X, Y):
  Z = inv(X.T*X)
  return Z*X.T*Y

# generate `n` samples
n = 15

# exponent
m = 8

x = np.arange(0,n,1)

# theory
z = .5*x*(x+1)

# generate output function
y = np.cumsum(x**m)
# format output
y.shape = (n,1)
Y = np.asmatrix(y)

# prepare matrix
X = np.ones((n,1))

x.shape = (n,1)

# add column of input until m+1 (inclusive)
for i in range(1, m+2):
  X = np.append(X, x**i, axis =1)

X = np.asmatrix(X)
r = solveOLS(X, Y)
print r
print np.cumsum(r)

# m=0: (1,   1)
# m=1: (0, 1/2, 1/2)
# m=2: (0, 1/6, 1/2, 1/3)
# m=3: (0,   0, 1/4, 1/2,  1/4)
# m=4: (0,   -1/30,   0, 1/3,  1/2, 1/5)  
# m=5: (0,   0,   0,   0, 5/12, 1/2, 1/6)
# 
# sum always 1!!? (except for 0)