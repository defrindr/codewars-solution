def binary_array_to_number(arr):
	print eval('0b'+''.join(str(a) for a in arr))


binary_array_to_number([1,1,1,1])