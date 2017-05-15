#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

max_sum = -23622320128

for i in range(6 - 2):
	for j in range(6 - 2):
		hg_sum = sum(arr[i][j:j+3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j+3])
		max_sum = max(max_sum, hg_sum)

print(max_sum)