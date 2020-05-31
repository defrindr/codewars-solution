def comb(fruits):
	n = []
	_tmp = 0
	if len(fruits) ==1 :
		return 0
	else:
		for i in xrange(0,len(fruits)-1):
			if i == 0 :
				_tmp = fruits[i] + fruits[i+1]
			else:
				_tmp += fruits[i+1];
			n.append(_tmp)
	return n

print comb([11, 9, 20, 10, 21, 35, 15, 34, 48, 76, 94, 28, 79, 16, 4, 41, 98, 30, 35, 92, 93, 33, 100, 93, 64, 23, 37, 6, 86, 27, 48, 16, 66, 99, 61, 83, 3, 5, 95])
