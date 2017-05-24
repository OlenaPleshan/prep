import sys

_A_LETTER_LOWER_CASE_ORD = ord('a')

def IsPalindrome(string):
	string = string.lower().replace(" ", "")
	character_count = {'odd': [], 'even': []}
	for c in string:
		if c in character_count['odd']:
			character_count['odd'].remove(c)
			character_count['even'].append(c)
		else:
			character_count['odd'].append(c)
	if len(character_count['odd']) > 1:
		return False
	return True

def IsPalindrome2(string):
	string = string.lower().replace(" ", "")
	bitmap = [0 for i in range(0, 26)]
	found_odd = False
	for c in string:
		char_position = ord(c)-_A_LETTER_LOWER_CASE_ORD
		bitmap[char_position] += 1
	for c in bitmap:
		if c % 2 == 1:
			if found_odd:
				return False
			found_odd = True	
	return True
	

print IsPalindrome(sys.argv[1])
print IsPalindrome2(sys.argv[1])
