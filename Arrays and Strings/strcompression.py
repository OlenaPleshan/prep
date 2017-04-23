import sys

def CompressString(original):
	new_string_array = []
	count_consecutive = 0
	i = 0
	while i < len(original):
		count_consecutive += 1
		if i+1 >= len(original) or not original[i] == original[i+1]:
			new_string_array.append(original[i])
			if count_consecutive > 1:
				new_string_array.append(str(count_consecutive))
			count_consecutive = 0
		i += 1
	return "".join(new_string_array)

print CompressString(sys.argv[1])
