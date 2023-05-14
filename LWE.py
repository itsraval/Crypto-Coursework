import numpy as np

def changeS():
	global s
	global m 
	global q
	i = input(f"The size of the secret vector does not match per parameter {m}!\nPres\n- [s] to generate a random secret vector\n- [any other key] to quite the program\n")
	if i == 's':
		s = np.random.randint(0, high=q, size=(m,1))
		print(f"New secret vector:\n{s}\n")
	else:
		exit()

def checkS():
	global s
	global m 
	global q
	if len(s) != m:
		changeS()
	for i in s:
		if i >= q:
			changeS()
	return 

n = 512
m = 20
q = 97

A = np.random.randint(0, high=q, size=(n,m))
s = np.array([[5], [ 8], [ 7], [ 3]])
e = np.random.randint(-1, high=2, size=(n,1))

checkS()

b = np.matmul(A, s)%q
b = np.add(b, e)%q
print(f"A: {A}\n")
print(f"s: {s}\n")
print(f"e: {e}\n")
print(f"b: {b}")