"""
 modelize plan trajectory with spline

Speed modeled as follow:
 - sin at beginning (0 to Vc)
 - vc
 - sin at end (Vc to 0)

Trajectory is derived by taking integral
"""

import numpy as np



tf = 10

t1 = 3
t2 = tf - t1
w = np.pi/t1
p1 = np.pi + np.pi/2. # phase so we can use only sin
p2 = np.pi/2.

# average speed / cruise speed
vc = 1000


# generic sin function so it does not need to be rewritten
def genSin(t, w, p, vc):
  return vc/float(2)*(np.sin(w*t+p)+1)

# integral primitive of previous function
def genSinPrim(t, w, p, vc):
  return vc/float(2)*(-np.cos(w*t+p)/w+t)


def f1(t):
  return genSin(t, w, p1, vc)

def f2(t):
  return vc

def f3(t):
  return genSin(t-t2, w, p2, vc)

def f(t):
  if t < 0:
    return 0
  if t < t1:
    return f1(t)
  elif t < t2:
    return f2(t)
  elif t < tf:
    return f3(t)
  else:
    return 0

    
######### calculates integrals ########

def f1Prim(t):
  return genSinPrim(t, w, p1, vc)

def f2Prim(t):
  return vc*(t-t1) + f1Prim(t1)

def f3Prim(t):
  return genSinPrim(t-t2, w, p2, vc) + f2Prim(t2)

def fPrim(t):
  if t1> tf/float(2):
    0
  else:
    if t < 0:
      return 0
    if t < t1:
      return f1Prim(t)
    elif t < t2:
      return f2Prim(t)
    elif t < tf:
      return f3Prim(t)
    else:
      return f3Prim(tf)

# compute integral numerically
def fNumPrim(t):
  N = 300  # number of iteration per call (very computational intensive)
  x = np.linspace(0,t,N)
  r = 0.
  dx = float(t)/float(N)
  for i in x:
    r = r + dx*g(i)

  return r


# piece of magic here
# http://scicomp.stackexchange.com/questions/1144/how-can-i-plot-piece-wise-defined-function-in-some-easily-accessed-open-source-t?newreg=3991fda29a504478a7aca2bb58e61b96
g = np.vectorize(f)
gPrim = np.vectorize(fPrim)
#gNumPrim = np.vectorize(fNumPrim)
  


import matplotlib.pyplot as plt

t = np.linspace(0, tf, 300)


plt.plot(t, g(t))


#plt.plot(t, gNumPrim(t))
plt.plot(t, gPrim(t))

plt.xlabel('time [s]')
plt.ylabel('trajectory [m]')
plt.legend()
plt.savefig("ballistic.png")
plt.show()