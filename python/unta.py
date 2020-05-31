import re
def to_camel_case(text):
	word = ''
	result = ''
	word = re.compile("-|_").split(text)
	for i in range(len(word)):
		if i == 0:
			result +=word[i]
		else:
			result +=word[i].title()
	print result



to_camel_case("the_stealth_warrior")