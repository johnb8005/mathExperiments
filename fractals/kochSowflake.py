"""
  Generate Koch Snowflake
"""

import svgwrite
import numpy as np

(h,w) = (700, 1500)

svg = svgwrite.Drawing(filename = "kochSnowflake.svg", size = (str(w)+"px", str(h)+"px"))


def addLine(c1, c2):
  svg.add(svg.line(c1, c2, stroke=svgwrite.rgb(10, 10, 16, '%')))


def addVectorToPoint(pt, v):
  return (pt[0]+v[0], pt[1]+v[1])


def addPolarVectortoPoint(pt, v):
  r     = v[0]
  theta = v[1]

  x = r*np.cos(theta)
  y = r*np.sin(theta)

  return addVectorToPoint(pt, (x,y))



def find4NextPts(pt, l ,alpha):
  pt1 = addPolarVectortoPoint(pt, (l/3,alpha))
  pt2 = addPolarVectortoPoint(pt1,(l/3, alpha-np.pi/3)) 
  pt3 = addPolarVectortoPoint(pt, (2*l/3,alpha))

  pt4 = addPolarVectortoPoint(pt, (l, alpha))

  return (pt1, pt2, pt3, pt4)


# length of triangle side
l = 210

# inital point
pt1 = (100,100)

# initial angle
alpha = 0

# depth of complexity
depth = 2
# number of points
n = 3*(4**(depth-1))
pts = np.empty([n,2])

# angle increment when going to a new side (do not change)
alphainc = np.pi/2+np.pi/6

ppt = pt1
for i in range(0,3):
# find 1/3, 1/2 and 2/3 of section
  alpha = i*alphainc
  pts[i*4:(i*4+4),:] = find4NextPts(ppt, l, alpha)
  ppt = pts[i*4+3]

ppt = pt1
for pt in pts:
  addLine(ppt, pt)
  ppt = pt



svg.save()