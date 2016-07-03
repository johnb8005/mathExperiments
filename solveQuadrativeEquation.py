"""
  solves 2nd degree equation
"""

import sys
import numpy as np


# check if right amount of arguments
if len(sys.argv) != 4:
  raise ValueError('The number of arguments must be 3')
  sys.exit()

try:
  (a,b,c) = (complex(sys.argv[1]),complex(sys.argv[2]),complex(sys.argv[3]))
except ValueError:
  raise NameError('Arguments could not be converted to numbers')

print a
print b
print c

d = (b**2 - 4*a*c)
print d
print 
x1 = (-b + np.sqrt(d))/2
x2 = (-b + np.sqrt(d))/2

# display nicely
np.set_printoptions(precision=2)
print np.array([x1, x2])