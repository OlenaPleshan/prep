import sys
import re

def Replace(string):
	return string.replace(" ", "%20")

def Replace1(string):
	return re.sub(r"\s", "%20", string)

def Replace2(string):
	return "".join(["%20" if c == " " else c for c in string])

print Replace(sys.argv[1])
print Replace1(sys.argv[1])
print Replace2(sys.argv[1])

