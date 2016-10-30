"""
  relation between the length of material coiled around cylinder and its width (toilet paper)
  http://math.stackexchange.com/questions/1633704/the-length-of-toilet-roll
"""
import numpy as np

x = 1 # width of one sheet
w = 80 #partial radius (total radius - minus radius of paper tube)
r = 30 # radius of paper tube

L = (np.pi/x)*w*(w+x+2*r)

print L