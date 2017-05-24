import sys

def IsPermutation(str1, str2):
	if len(str1) != len(str2):
		return False
	dict1 = {}
	dict2 = {}
	for i in range(len(str1)):
		if str1[i] in dict1.keys():
			dict1[str1[i]] += 1
		else:
			dict1[str1[i]] = 1
		if str2[i] in dict2.keys():
			dict2[str2[i]] += 1
		else:
			dict2[str2[i]] = 1
	if not cmp(dict1, dict2):
		return True
	return False

def IsPermutation2(str1, str2):
	if len(str1) != len(str2):
		return False
	if not "".join(sorted(str1)) == "".join(sorted(str1)):
		return False
	return True

print IsPermutation(sys.argv[1], sys.argv[2])
print IsPermutation2(sys.argv[1], sys.argv[2])

# or you could sort the strings and compare them.
# If the same, return True, otherwise False.
