# Find if a number k is prime or not

def is_prime(k):
    #vec = range(k)
    out = True
    for i in xrange(2, k):
        if(k % i == 0):
            out = False
    return(out)


for i in xrange(32): print i, is_prime(i)
