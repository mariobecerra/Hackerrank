# Tienes un arreglo y un numero k. Encontrar dos numeros del arreglo que sumen k.

import time
import math

k = int(raw_input())
array = map(int, raw_input().strip().split(' '))
n = len(array)

start = time.time()

array = sorted(i for i in array if i < k)

out = False
flag = True

i = 0
n1 = n - 1
while(flag):
	x = array[i] + array[n1]
	if x == k:
		out = True
		break
	elif x < k:
		i += 1
	else:
		n1 -= 1
	if n1 < math.floor(n/2) or i > math.ceil(n/2):
		flag = False

end = time.time()

print out
print(end - start)