# Extra Long Factorials

# https://www.hackerrank.com/challenges/extra-long-factorials/problem


import sys


n = int(input().strip())

def fact2(n):
    vec = range(2, n+1)
    aux = 1
    for i in vec:
        aux = aux*i
    print(aux)

fact2(n)
    
