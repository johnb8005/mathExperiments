""""
  This script solves the famous "fold piece of paper to the moon" problem

  Problem description: how many times would you have to fold a piece of paper onto itself to reach the Moon?
"""

import numpy as np


# paper width in meters: 0.1 mm
paperWidth = 0.1*10**-3

# distance earth moon: 384,400 km
distance = 384400*10**3

# equation can be formulated as : 2^n w = d

n = np.log(distance/paperWidth)/np.log(2)

# display nicely
np.set_printoptions(precision=2)
print np.array([n])