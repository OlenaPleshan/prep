import sys

def hasUniqueCharacters(string):
	endOfString = len(string) - 1
	for i, s in enumerate(string):
		j = endOfString
		while i < j:
			if s == string[j]:
				return False
			j -= 1;
	return True

print hasUniqueCharacters(sys.argv[1])
