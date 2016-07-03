"""
  Simulation of the roulette game
"""

from random import randint

import math
import numpy as np

"""
  @return: {even: 0, odd: 1, zero: -1}
"""
def evenOrOdd(x):
  if x==0:
    return -1;
  else:
    if x % 2 == 0:
      return 0
    else:
      return 1

"""
  @param x:     black or white
  @param preva: 
  @param prevb: 
"""
def placeBet(x, preva, prevb):
  m = 0 
  p = 4 # amount of time allowed to follow the martingale principle

  # check if same result more than `m` times
  if preva >= m: #and preva <= m+p:
    mult = 2**(preva-m+1)
    if evenOrOdd(x) == prevb:
      return -mult
    else: 
      return +mult
  else:
    return 0

def runSerie(n):
  # number iteration same
  preva = 0
  # bow result
  prevb = 0

  credit = 0

  for i in range(0, n):
    draw = randint(1,36)
     # black or white: bow
    bow = evenOrOdd(draw)

    bet = placeBet(bow, preva, prevb)
    credit += bet

    # prepare for next iteration
    # count number of same outcome
    if prevb == bow:
      preva+=1
    else:
      preva=0

    # assign previous result to `prevb`
    prevb = bow
  # end loop

  return credit

# number of games
n = 100
m = 1

credit = np.empty(m)

for i in range(0,m):
  credit[i] = runSerie(n) 

print(credit)

np.set_printoptions(precision=2)
print np.array([n])
print np.array([np.sum(credit), np.mean(credit), np.std(credit)])

