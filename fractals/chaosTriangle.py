"""
  chaos triangle
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

def addCircle(c, r):
  svg.add(svg.circle(
    center = c, r=r, 
    stroke_width = "1",
    stroke = "black",
    fill = "white"
  ))


def drawPoint(s):
  addCircle(s, .81)


(h,w) = (700, 1500)

svg = svgwrite.Drawing(filename = "chaosTriangle.svg", size = (str(w)+"px", str(h)+"px"))

c1 = (300, 600)
c2 = (1100, 200)
c3 = (900, 600)
c4 = (100, 200)
c5 = (600, 50)

c = [c1, c2, c3, c4, c5]

#addTriangle(c1, c2, c3)


# generate random point
s = (550, 200)


drawPoint(s)

i = 0
n = 100000
clen =len(c)

while(i < n):
  r = random.randrange(clen)
  s = middlePoint(s, c[r])
  drawPoint(s)
  i+=1


svg.save()