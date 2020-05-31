def longest_palindrome (real):
	reverse = real[::-1]
	same = 0
	for i in range(len(real)):
		if real[i] == reverse[i]:
			same+=1
	print same

longest_palindrome("a") #, 1
longest_palindrome("aa") #, 2
longest_palindrome("baa") #, 2
longest_palindrome("aab") #, 2
longest_palindrome("abcdefghba") #, 1
longest_palindrome("baablkj12345432133d") #, 9
