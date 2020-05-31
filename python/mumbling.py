def accum(s):
	b = []
	for a in range(len(s)):
		b.append(str(s[a]*(a+1)).title())
	print '-'.join(c for c in b)
accum("ZpglnRxqenU")
