import numpy as np 

"""
  converts polar coordinates (r, theta) to cartesian (x,y)
"""
def polarToCartesian(p):
  r     = p[0]
  theta = p[1]

  x = r*np.cos(theta)
  y = r*np.sin(theta)
  return np.array([x, y])

"""
  converts cartesian (x,y) to polar coordinates (r, theta)
"""
def cartesianToPolar(s):
  x = s[0]
  y = s[1]

  r = np.sqrt(s[0]**2 + s[1]**2)
  theta = np.arctan2(y,x)

  return np.array([r, theta])


"""
  solved 2nd degree equation
"""
def solve2ndDegEq(a,b,c):
  d = (b**2) - 4*a*c
  x = np.sqrt(complex(d))
  return (-b + np.array([x,-x]))/(2*a)


#x = np.array([1,0])
#y = cartesianToPolar(x)
#print polarToCartesian(y)