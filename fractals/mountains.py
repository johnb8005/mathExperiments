"""
  mountains
"""
import svgwrite
import random

def addLine(c1, c2):
  svg.add(svg.line(c1, c2, stroke=svgwrite.rgb(10, 10, 16, '%')))

def addTriangle(c1, c2, c3):
  addLine(c1, c2)
  addLine(c1, c3)
  addLine(c2, c3)

def middlePoint(c1, c2):
  a1 = (c1[0] + c2[0])/2
  a2 = (c1[1] + c2[1])/2
  return (a1, a2)

def randomOnLine(c1, c2):
  w = random.random()

  x = w*(c2[0]-c1[0])+c1[0]

  m = (c1[1] - c2[1])/(c1[0]-c2[0])
  q = c1[1] - m*c1[0]

  y = m*x + q

  return (x, y)

(h,w) = (700, 1500)

svg = svgwrite.Drawing(filename = "mountains.svg", size = (str(w)+"px", str(h)+"px"))

c1 = (100, 600)
c2 = (400, 100)
c3 = (1000, 600)

addTriangle(c1, c2, c3)



def toTwoTriangle2(c1, c2, c3, n):
  c4 =  randomOnLine(c1, c3) #middlePoint(c1, c3)

  addTriangle(c1, c2, c4)
  addTriangle(c3, c2, c4)

  if n > 1:
    toTwoTriangle(c1, c2, c4, n-1)
    toTwoTriangle(c3, c2, c4, n-1)


def toTwoTriangle(c1, c2, c3, n):
  # get random number
  r = random.randrange(3)
  # calculate new point
  

  if r == 1:
    toTwoTriangle2(c1, c2, c3, n)
  elif r ==2:
    toTwoTriangle2(c2, c3, c1, n)
  else:
    toTwoTriangle2(c3, c1, c2, n)

toTwoTriangle(c1, c2, c3, 2)


#print c5
#print c6

#addLine(c2, c4)

#addLine(c4, c5)

#addLine(c5, c6)
#
# c1, c2, c3
# c1, c2, c4

svg.save()