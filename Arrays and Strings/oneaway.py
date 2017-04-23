import sys

def IsOneAway(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	diff = len1 - len2
	if abs(diff) > 1:
		return False

	nr_edits = 0
	for i, s in enumerate(str1):
		j = i-diff if nr_edits > 0 and abs(diff) == 1 else i
		if not str2[j] == s:
			nr_edits += 1
		if nr_edits > 1:
			return False
	return True

print IsOneAway(sys.argv[1], sys.argv[2])
