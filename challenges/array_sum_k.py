# Tienes un arreglo y un numero k. Encontrar dos numeros del arreglo que sumen k.

import time

k = int(raw_input())
array = map(int, raw_input().strip().split(' '))

n = len(array)

start = time.time()

out = False
for i in range(n):
	for j in range(i, n):
		if(array[i] + array[j] == k):
			out = True

end = time.time()

print out
print(end - start)

