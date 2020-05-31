def rot(strOld):
	strList = list(strOld.split('\n'))[::-1]
	newList = []
	revStr = ''
	for strNum in strList:
		revStr = strNum[::-1]
		newList.append(revStr)
	return '\n'.join(newList)

def selfie_and_rot(strOld):
	strList = list(strOld.split('\n'))
	newList = []
	revStr = ''
	addPoint = len(max(strList))
	for num in range(len(strList)):
		strList[num] = strList[num]+"."*addPoint
		revStr = strList[num][::-1]
		newList.append(revStr)
	return '\n'.join(strList)+"\n"+'\n'.join(newList[::-1])

def oper(fct,s):
	fct(s)

oper(rot,"abcd\nefgh\nijkl")