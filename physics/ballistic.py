"""
  elementary ballistic problem
"""

import numpy as np
from scipy import constants
import helper


### constants ###

# gravity
g = constants.gravitational_constant

### end constants ###

### initial conditions ###


# initial position
x0 = 0
y0 = 125 
s0 = (x0,y0)
# scalar inital speed
v0s = 12
# angle 
theta = np.pi/6 
# define acceleration vector - acceleration is constant here
a = np.array([0, -g])

### end initial conditions ###


# from initial condition get vector form of speed
v0 = helper.polarToCartesian(np.array([v0s, theta]))


print "a:  "+str(a)
print "v0: "+str(v0)
print "s0: "+str(s0)


"""
  speed in function of time

  @arg t: time
  @return v: speed
"""
def v(t):
  return a*t+v0


"""
  position in function of time

  @arg t: time
  @return s: position
"""
def s(t):
  return .5*a*(t**2) + v0*t + s0


"""
  find time in function of x
  @return t
  @param x: position
"""
def tFromX(x):
  return (x-s0[0])/v0[0]

"""
  get position (x and y) from x
"""
def sfromX(x):
  return s(tFromX(x))

"""
  find time in function of y
  @return t
  @param y: position
"""
def tFromY(y):
  s = helper.solve2ndDegEq(.5*a[1], v0[1], s0[1]-y) # solve 2nd deg equation
  f = max(s) # take max of two results (most likely is the other negative)
  return f.real # and return real part to avoid confussion


"""
  find t that maximizes height
"""
tMaxHeight = -v0[1]/a[1]

"""
  computes associated position
"""
sMaxHeight = s(tMaxHeight)
print "Missile reaches highest point at time "+str(tMaxHeight)+" and position "+str(sMaxHeight)

"""
  find t when y=0
"""

tZeroHeight = tFromY(0)
sZeroHeight = s(tZeroHeight)


print "Missile reaches floor at time "+str(tZeroHeight)+" and position "+str(sZeroHeight)

print tFromX(6.3561497)
print sfromX(6.3561497)
print tFromY(126.83486239)
