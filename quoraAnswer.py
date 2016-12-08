""" answer to """
import numpy as np


# terminiology: 
# - segment are prefixed by `s` and followed by upper case nodes: e.g. `sAB` is the length of the semgnet from A to B
# - angles are prefixed with `ang` and followed by upper case nodes: e.g. `angABC` is the angle between A, B, and C
# - area are prefixed with `area` and followed by upper case ndes: e.g. `areaABC` is the area comprised between nodes A, B, and C
# 
# new defintions:
# - we define a new node H, between A and B so that angAHC = angDHC = 90 deg


## helper function to convert ang to rad and reverse
def angToRad(ang):
  return ang*np.pi/180

def radtoAng(rad):
  return rad/np.pi*180
## end helper

# var definition
angCAD = angToRad(80)
angDCB = angToRad(25)

# var from the exercise
sAB = 4.9
sAD = 3.8

# get height length
sHC = sAB * np.sin(angCAD)
# get distance from A to H
sAH = sAB * np.cos(angCAD)
# get distance from H to D
sHD = sAD - sAH

# get angle HCD
angHCD = np.arctan(sHD / sHC)
# get angle HCB
angHCB = angHCD + angDCB

# get HB
sHB = sHC * np.tan(angHCB)
# get distance from A to B
sAB = sAH + sHB

# get two triangles areas
areaACD = sHC * sAD / 2
areaACB = sAB * sHC / 2

# get asked area
areaDCB = areaACB - areaACD

print areaDCB