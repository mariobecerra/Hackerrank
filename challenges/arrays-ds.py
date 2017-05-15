# Arrays - DS
# https://www.hackerrank.com/challenges/arrays-ds

import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split())

#out = []
for i in xrange(n):
	#out.append(arr[n - i - 1])
	print(arr[n - i - 1]),

#print(out)	