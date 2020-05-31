# def year_max_people(n):
# 	s = 0
# 	_tmp = 0
# 	__tmp = 0
# 	u = 0
# 	for i in range(len(n)):
# 		print n[i][1] - n[i][0]
# 	# 	if __tmp < _tmp :
# 	# 		__tmp =  _tmp
# 	# 		s = n[i][0]
# 	# for i in range(len(n)):
# 	# 	if n[i][0] == s :
# 	# 		u = i
# 	# print (u,s)
# year_max_people([(1980, 2010), (1979, 1985), (1986, 1995), (1987, 2008)]) #(3, 1987)
##year max people
#
#
#
#
#
a = [20,8,5,19,21,14,19,5,20,19,5,20,19,1,20,20,23,5,12,22,5,15,3,12,15,3,11]

for i in range(len(a)):
	a[i] = a[i]+64

print a
