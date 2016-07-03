#!/usr/bin/perl



xmin = 1
xmax = 150
x    = xmin

while x <= xmax:
  y=1

  while y <= 80:
    z=1
    while z <= 80:
      if x*y*z == x**2 + y**2 +z**2:
        print "The combination is: x="+str(x)+"\ty: "+str(y)+"\tz: "+str(z)
      
      z += 1
    y += 1
  x += 1
  