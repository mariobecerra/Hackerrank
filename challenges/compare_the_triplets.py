#!/bin/python

# Compare the Triplets
# https://www.hackerrank.com/challenges/compare-the-triplets

import sys

a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
# Write Your Code Here

A = 0
B = 0

if(a0 > b0): A = A + 1
elif(a0 < b0): B = B + 1

if(a1 > b1): A = A + 1
elif(a1 < b1): B = B + 1

if(a2 > b2): A = A + 1
elif(a2 < b2): B = B + 1

print str(A) + " " + str(B)

