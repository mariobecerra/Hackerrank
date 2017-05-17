
string = raw_input()

flag = True
i = 0

def reverse(string):
	n = len(string)
	out = [' ' for i in range(n)]
	for i in range(n):
		out[i] = string[n - i - 1]
	return ''.join(out)

n = len(string)
out = ''

while(flag):
	j = i
	string_aux = string[j + 1]
	out = out + string[i]
	while(string_aux != '(' and string_aux != ')'):
		j += 1
		string_aux = string[j + 1]
	#print string[i],
	out = out + reverse(string[(i + 1):(j + 1)])
	i = j + 1
	if(i >= (n - 1)): 
		break

out = out + string[n - 1]

print out