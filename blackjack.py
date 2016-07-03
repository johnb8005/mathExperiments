"""
  simulates blackjack
"""

from random import randint
import numpy as np

"""
  draw a card from the deck
  1: as
  2-10: 2-10
  11: jack
  12: queen
  13: king
"""
def draw():
  return randint(1,13)

"""
  param x: card type, see `draw` for legend
  return card point
"""
def points(x):
  if x > 0 and x < 10:
    return x
  else:
    return 10

def scoreFromVector(arr):
  score = 0 # score
  aces = 0 # counts aces (possibility to add 10)
  for k,v in np.ndenumerate(arr):
    score += points(v)
    if v == 1:
      aces += 1


  # need to find optimal score
  if aces > 0 and score <= 21 - 10:
    score += 10


  # see if lost
  lost = score > 21

  return (score, lost)


# dealer card deck
dealer = np.array([])
player = np.array([])


stop = False
while stop == False:

  dealer = np.append(dealer, draw())
  player = np.append(player, draw())

  #print player
  player_score = scoreFromVector(player)
  dealer_score = scoreFromVector(dealer)

  print player_score
  print dealer_score

  prompt = '> '
  print "Would you like to continue?"
  likes = raw_input(prompt)
  print likes
  if int(likes) > 2:
    stop = True


