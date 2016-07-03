"""
  Generate timetable
  https://www.youtube.com/watch?v=qhbuKbxJsk8
"""
 
import svgwrite
import numpy as np

svg = svgwrite.Drawing(filename = "test-svgwrite.svg",
                                size = ("1000px", "1000px"))


(cx,cy,cr) = (300,300,280)






def coordFromAngle(alpha):
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
def calculateCoordinate(n, pts):
  coords = np.empty([n,2])
  for (idx,angle) in enumerate(pts):
    coords[idx] = coordFromAngle(angle)  
  return coords



# add surrounding circle
addCircle((cx,cy), cr)


# number of points around circle
n = 1202
# multiplicative factor
m = 69
pts = np.linspace(0, 2*np.pi, n)

# get coords for all points
coords = calculateCoordinate(n, pts)

for (idx,angle) in enumerate(pts):

  idx2 = idx*m%n

  addLine(coords[idx], coords[idx2])

#for (idx,angle) in enumerate(pts):

  #addCircle(coords[idx], 3)



#svg.add(svg.text("Hello World",
                             #      insert = (210, 110)))

print(svg.tostring())

svg.save()