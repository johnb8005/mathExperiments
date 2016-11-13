"""
  Drawing star from 2 circles
"""
 
import svgwrite
import numpy as np

(h,w) = (700, 1500)

svg = svgwrite.Drawing(filename = "simpleStar.svg", size = (str(w)+"px", str(h)+"px"))

def coordFromAngle(alpha, cr):
  x = cr*np.cos(alpha) + cx
  y = cr*np.sin(alpha) + cy
  return (x,y)


def addLine(c1, c2):
  svg.add(svg.line(c1, c2, stroke=svgwrite.rgb(10, 10, 16, '%')))

def addCircle(c, r, stroke = "black"):
  svg.add(svg.circle(
    center = c, r=r, 
    stroke_width = "1",
    stroke = stroke,
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


def getPointsAroundCircle(cc, r, n, phase):
  """
    return points equidistributed around circle of radius `r`
  """
  angles = np.linspace(0, 2*np.pi, n+1) + phase
  return calculateCoordinate(angles, r)

def drawPointsAsCircle(coords, r = 3, color = "black"):
  """
    draw list of points (coords) as circle of radius `r`
  """
  for (idx,angle) in enumerate(coords):
    addCircle(angle, r, color)

def linkArraysWithLines(cp1, cp2):
  """
    links two arrays of coordinates (same size) with lines
  """
  for (a,b) in zip(cp1, cp2):
    addLine(a,b)


def drawStar(c, rs, n, origPhase):
  (cx,cy) = c
  (r1, r2) = rs

  #addCircle((cx,cy), r1)
  #addCircle((cx,cy), r2)

  cp1 = getPointsAroundCircle((cx, cy), r1, n, origPhase)
  cp2 = getPointsAroundCircle((cx, cy), r2, n, origPhase + np.pi/n)
  # moves first coordinates at end of array to shift order and print missing lines
  cp3 =  np.vstack((cp1[1:-1][:], cp1[0][:]))

  #drawPointsAsCircle(cp1)
  #drawPointsAsCircle(cp2)

  linkArraysWithLines(cp1, cp2)
  linkArraysWithLines(cp3, cp2)

# main circle coorindates
(cx,cy,cr) = (w/2,h/2,280)


# number of points around circle
n = 7
origPhase = -np.pi/2 # begins at top of cirlce instead of on the side

# draws many star with different ratios to outer circle
for alpha in np.linspace(0, 2, 201):
  drawStar((cx, cy), (cr, alpha*cr), n, origPhase)

#drawStar((cx, cy), (cr, .5*cr), n, origPhase)
#drawStar((cx, cy), (cr, .6*cr), n, origPhase)

svg.save()