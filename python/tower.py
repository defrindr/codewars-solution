def tower_builder(n):
    a = []
    g=[]
    __a =n
    for _a in range(1000):
    	if _a % 2 != 0:
    		g.append(_a)
    for i in range(n):
    	if i != n-1:
    		a.append(str(" "*((n-1)-i))+str("*"*g[i])+str(" "*((n-1)-i)))
    	else:
    		a.append("*"*g[i])
    		pass
    return a

tower_builder(3)

# ['   *   ',
#  '  ***  ',
#  '*****']