# Sparse arrays
# https://www.hackerrank.com/challenges/sparse-arrays


# Enter your code here. Read input from STDIN. Print output to STDOUT# There are  strings. Each string's length is no more than 20 characters. 
# There are also Q queries. 
# For each query, you are given a string, and you need to find out how many times this string occurred previously.

# Input Format

# The first line contains , the number of strings.
# The next  lines each contain a string.
# The nd line contains , the number of queries.
# The following  lines each contain a query string.

n = int(raw_input().strip())
strings = []
arr = []
for i in range(n):
	strings.append(raw_input().strip())

q = int(raw_input().strip())
queries = []
for i in range(q):
	queries.append(raw_input().strip())
	arr.append(0)

i = 0
for x in queries:
	for y in strings:
		if(x == y): arr[i] += 1
	i += 1

for i in range(q):
	print(arr[i])