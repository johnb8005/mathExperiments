"""
  Generate Koch Snowflake
"""

import svgwrite
import numpy as np

(h,w) = (700, 1500)

svg = svgwrite.Drawing(filename = "kochSnowflake.svg", size = (str(w)+"px", str(h)+"px"))


def addLine(c1, c2):
  svg.add(svg.line(c1, c2, stroke=svgwrite.rgb(10, 10, 16, '%')))


def middlePoint(c1, c2):
  return ptRatiofSegment(c1, c2, .5)

def ptRatiofSegment(c1, c2, a):
  x = a*(c2[0] - c1[0]) + c1[0]
  y = a*(c2[1] - c1[1]) + c2[1]
  return (x,y)

def slope(c1, c2):
  return (c2[1] - c1[1])/(c2[0] - c1[0])

def addVectorToPoint(pt, v):
  return (pt[0]+v[0], pt[1]+v[1])


def addPolarVectortoPoint(pt, v):
  r     = v[0]
  theta = v[1]

  x = r*np.cos(theta)
  y = r*np.sin(theta)

  return addVectorToPoint(pt, (x,y))


def calculateH(l):
  return l/np.sqrt(12)


print np.sin(np.pi/3)
print np.sqrt(3)/2


l = 180
pt1 = (20,80)
pt2 = (l+pt1[0], pt1[1])
pt3 = addPolarVectortoPoint(pt2, (180, np.pi/2+np.pi/6))


addLine(pt2, pt3)
addLine(pt3, pt1)


# find 1/3, 1/2 and 2/3 of section
pt11 = addPolarVectortoPoint(pt1, (l/3,0))#  (pt1[0]+l/3, pt1[1]) #ptRatiofSegment(pt1, pt2, 1/3)
pt13 = addPolarVectortoPoint(pt1, (2*l/3,0)) #(pt1[0]+2*l/3, pt1[1])

h = -calculateH(l)
print h
pt14 = addPolarVectortoPoint(pt11, (l/3, -np.pi/3))

addLine(pt1,  pt11)
addLine(pt11, pt14)
addLine(pt14, pt13)
addLine(pt13, pt2)


#pt6 = addPolarVectortoPoint(pt5, (180, np.pi+np.pi/3))




svg.save()