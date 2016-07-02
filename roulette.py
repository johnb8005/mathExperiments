"""
  Simulation of the roulette game
"""

from random import randint

import math
import numpy as np

# number of games
n = 100


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

def placeBet(x, preva, prevb):
  m = 0
  p = 4 # amount of time allowed to follow the martingagle principle
  if preva >= m: # and preva <= m+p:
    mult = math.pow(2, preva-m+1)
    if evenOrOdd(x) == prevb:
      return -mult
    else: 
      return +mult
  else:
    return 0


r = [1,1,1,2, 3, 3, 3, 3, 2]

n = 100 #len(r)


def runSerie(n):
  # number iteration same
  preva = 0
  # bow result
  prevb = 0

  credit = 0

  #print " bow\tbow-1\tpreva\tbet\tcredit"

  for i in range(0, n):
    draw = randint(1,36)
     # black or white
    bow = evenOrOdd(draw)

    bet = placeBet(bow, preva, prevb)
    credit += bet
    #print " "+str(bow)+"\t"+str(prevb)+"\t"+str(preva)+"\t"+str(bet)+"\t"+str(credit)


    # prepare for next iteration
    if prevb == bow:
      preva+=1
    else:
      preva=0

    

    prevb = bow
  # end loop
    
  return credit


m = 10000
credit = np.empty(m)

for i in range(0,m):
 credit[i] = runSerie(100)
 

print(credit)

np.set_printoptions(precision=2)
print np.array([n])
print np.array([np.sum(credit)])
