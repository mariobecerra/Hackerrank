#!/bin/python

# Diagonal difference
# https://www.hackerrank.com/challenges/diagonal-difference

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

sum1 = 0
sum2 = 0
for i in range(0, n):
	sum1 = sum1 + a[i][i]
	sum2 = sum2 + a[i][n - i - 1]

print(abs(sum1 - sum2))	
