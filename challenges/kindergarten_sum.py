# Given two arrays, save the result of the sum in another array in kindergarten style

array1 = map(int, raw_input().strip().split(' '))
array2 = map(int, raw_input().strip().split(' '))

n1 = len(array1)
n2 = len(array2)


# def make_sum_aux(array1, array2, n):
# 	array_out = [0 for i in range(n + 1)]
# 	for i in xrange(n):
# 		aux = array1[i] + array2[i]
# 		if aux > 9:
# 			#carry = 1
# 			array_out[i + 1] += 1
# 			aux = aux - 10
# 		array_out[i] += aux
# 	return array_out


def make_sum(array1, array2, n1, n2):
	# Assumes array1 is longer than array2
	array_out = [0 for i in range(n1 + 1)]
	aux = 0
	# carry = 0

	for i in xrange(n2):
		aux = array1[n1 - i - 1] + array2[n2 - i - 1]
		if aux > 9:
			array_out[n1 - i - 1] += 1
			aux = aux - 10
		array_out[n1 - i] += aux

	for i in xrange(n2, n1): # n2 = 1, n1 = 4, # 1, 2, 3
		aux = array1[n1 - i - 1] + array_out[n1 - i]
		if aux > 9:
			array_out[n1 - i - 1] += 1
			aux = aux - 10
		array_out[n1 - i] = aux

	return array_out

if(n1 > n2):
	res = make_sum(array1, array2, n1, n2)
	if(res[0] == 0):
		print res[1:(n1 + 1)]
	else:
		print res
else:
	res = make_sum(array2, array1, n2, n1)
	if(res[0] == 0):
		print res[1:(n1 + 1)]
	else:
		print res

