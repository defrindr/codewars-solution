def rot13(message):
	_result = ''
	for a in message:
		if ord(a) >= 65 and ord(a) <= 77:
			c = ord(a)+13
			_result += eval("chr("+str(c)+")")
		elif ord(a) >= 78 and ord(a) <= 90:
			c = ord(a)-13
			_result += eval("chr("+str(c)+")")
		elif ord(a) >= 97 and ord(a) <= 109:
			c = ord(a)+13
			_result += eval("chr("+str(c)+")")
		elif ord(a) >= 110 and ord(a) <= 122:
			c = ord(a)-13
			_result += eval("chr("+str(c)+")")
		else:
			_result += a
	return _result

# rot13 = rot13("Qrsev Vaqen Znuneqvxn")
# print(rot13)
# Output : Defri Indra Mahardika
