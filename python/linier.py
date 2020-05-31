def dbl_linear(u):
	a= []
	for x in xrange(0,u):
		a.append(2*x+1)
		a.append(3*x+1)
	a = list(set(a))
	return a

print dbl_linear(10)