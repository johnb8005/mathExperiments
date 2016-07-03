"""
  solves 2nd degree equation
  to solve: x^2 -x - 90 = 0
  `python solveQuadrativeEquation.py 1 -1 -90`
"""

import sys
import numpy as np
import helper


# check if right amount of arguments
if len(sys.argv) != 4:
  raise ValueError('The number of arguments must be 3')
  sys.exit()

try:
  (a,b,c) = (complex(sys.argv[1]),complex(sys.argv[2]),complex(sys.argv[3]))
except ValueError:
  raise NameError('Arguments could not be converted to numbers')

x = helper.solve2ndDegEq(a,b,c)

# display nicely
np.set_printoptions(precision=2)
print x