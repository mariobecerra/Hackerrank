# Merge the tools
# https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in xrange(n/k):
        substring = string[k*i:(k*i + k)]
        strings_so_far = list()
        out = ''
        for letter in substring:
            if(not letter in strings_so_far): 
                out = out + letter
                strings_so_far.append(letter)
        print(out)
        
