# https://www.hackerrank.com/challenges/string-compression

# Example 1:
# Input: aaaaabbbbccdeff 
# Output: a5b4c2def2

# Example 2:
# Input: aaabaa
# Output: a3ba2

import sys

cadena = raw_input().strip()
cadena = cadena + " "
out = ""

num_i = 1
for i, c in enumerate(cadena):
	if(c == " "): break
	if(num_i == 1): out = out + c
	if(cadena[i + 1] == c): num_i += 1
	elif(num_i != 1):
		out = out + str(num_i)
		num_i = 1

print(out)