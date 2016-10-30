"""
  David Star
"""
 
import svgwrite
import numpy as np

(h,w) = (700, 1500)

svg = svgwrite.Drawing(filename = "davidstar.svg", size = (str(w)+"px", str(h)+"px"))

def coordFromAngle(alpha, cr):
  x = cr*np.cos(alpha) + cx
  y = cr*np.sin(alpha) + cy
  return (x,y)


def addLine(c1, c2):
  svg.add(svg.line(c1, c2, stroke=svgwrite.rgb(10, 10, 16, '%')))

def addCircle(c, r):
  svg.add(svg.circle(
    center = c, r=r, 
    stroke_width = "1",
    stroke = "black",
    fill = "white"
  ))


# calculate (x,y) coordinates for angles around circle
# param n: number of points
# param pts: list of points
def calculateCoordinate(pts, cr):
  n = len(pts)
  coords = np.empty([n,2])
  for (idx,angle) in enumerate(pts):
    coords[idx] = coordFromAngle(angle, cr) 
  return coords


def nrOnSegment(x,s):
  return x >= 0 and x <= s

def pointIsInFrame(c):
  return nrOnSegment(c[0], w) and nrOnSegment(c[1], h)

# calculates extended coordinates (lines come out of circle)
# arg c1, c2 two points on circle
def extendedCoordinates(c1, c2):
  # slope
  m = (c2[1]-c1[1])/(c2[0]-c1[0])
  q = c2[1] - m*c2[0]

  def y(x):
    return m*x + q

  def x(y):
    return (y - q)/m

  # calculates intersections with external boudary
  d1 = (0, y(0))
  d2 = (w, y(w))
  d3 = (x(0), 0)
  d4 = (x(h), h)

  l = np.array([d1,d2,d3,d4])

  # create array out
  r = np.empty([2,2])

  j = 0
  for pt in l:
    if pointIsInFrame(pt):
      r[j] = pt
      j += 1

  return r



# main circle coorindates
(cx,cy,cr) = (w/2,h/2,280)





# number of points around circle
n = 6

def printDavid(cr, m):

  factor = 1/np.sqrt(3)**m
  cr = factor*cr

  
  # add surrounding circle
  #addCircle((cx,cy), cr)
  angles = np.linspace(0, 2*np.pi, n+1)+np.pi/6*m
  coords = calculateCoordinate(angles, cr)

  # print points around circle
  #for (idx,angle) in enumerate(coords):
  #  addCircle(angle, 3)


  for i in range(0,n):
    addLine(coords[i], coords[(i+2)%n])




for m in range(0,10):
  printDavid(cr, m)


svg.save()