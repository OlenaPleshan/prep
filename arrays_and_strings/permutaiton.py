import sys

def IsPermutation(str1, str2):
	if len(str1) != len(str2):
		return False
	dict1 = {}
	dict2 = {}
	for i, c in enumerate(str1):
		dict1[i] += 1
		dict2[i] += 1
	print dict1
	print dict2
	if !cmp(dict1, dict2):
		return True
	return False

IsPermutation(sys.argv[1], sys.argv[2])
