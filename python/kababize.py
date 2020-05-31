import re
def kebabize(string):
	_str = ''
	a = list(re.findall(r'(.)', re.sub(r'\d','',string)))
	for i in a:
		if i.istitle():
			_str += '-'+''.join(i.lower())
		else :
			_str += ''.join(i)
	return _str.strip('-')