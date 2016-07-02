"""
  calculates probability of having a string made of number containing a 7 or a 8
"""


def bruteforce(m):
  "uses bruteforce method, goes through all possibility and iterate dummy variable if number contains {7,8}"
  n = 10**m

  c = 0
  for i in range(0,n):
    if str(7) in str(i) or str(8) in str(i):
      c += 1
      #print i
  
  return float(c)/float(n)


def analytical(n):
  "uses combinatorial law to find probability"
  m = 10 - 2
  return 1 -  (float(m)/float(10))**n


if __name__ == "__main__":
  # number of digits
  n = 4

  print "probability: "+str(bruteforce(n))
  print "probability: "+str(analytical(n))

  # additional info about problem:
  #  if `n` is the number of digits, 
  #  S the set of forbidden numbers, e.g. S = {7,8}, 
  #  V the set of allowed numbers, e.g. V = {0,1,2,3,4,5,6,7,8,9}
  #  the following property must be satisfied: S \in V
  #  we define `s` := |S|  (e.g. |{7,8}| = 2)
  #  we define `v` := |V|  (e.g. |{0,1,2,3,4,5,6,7,8,9}| = 10) 
  #  we then have
  #  f(n,v,s) = 1 - (s/v)^n
  #  or
  #  f(n,v,s) = 1 - exp(-ln(v/s)*n)