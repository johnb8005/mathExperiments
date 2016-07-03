"""
  Reciprocal Fibonacci constant
  script that computes the golden ratio form the sum of the reciprocals of the Fibonacci numbers
  @see https://en.wikipedia.org/wiki/Reciprocal_Fibonacci_constant
"""
x = 1
p1 = 1
p2 = 1

for i in range(1,50):
	x += 1.0/p2
	p2 += p1
	p1 = p2 - p1

	print str(i)+". "+str(p2)+"\t"+str(x)