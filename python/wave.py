def wave(strOld):
	_result = []
	for lenStr in range(len(strOld)):
		strNew = list(strOld)
		if strNew[lenStr] == " ":
			continue
		else:
			strNew[lenStr] = strNew[lenStr].title()
		_result.append(''.join(char for char in strNew))
	print _result

wave("hallo goblok")