#!/bin/python

# A Very Big Sum
# https://www.hackerrank.com/challenges/a-very-big-sum

import sys


n = int(raw_input().strip())
arr = map(long,raw_input().strip().split(' '))

print(sum(arr))
