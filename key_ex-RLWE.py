import numpy as np
from numpy.polynomial import polynomial as p

def gen_poly(n,q):
    global xN_1
    l = 0 
    poly = np.floor(np.random.normal(l,size=(n)))
    while (len(poly) != n):
        poly = np.floor(np.random.normal(l,size=(n)))
        poly = np.floor(p.polydiv(poly,xN_1)[1]%q)
    return poly

def extractError(shared):
	global u
	for i in range(len(u)):
		if (u[i] == 0):
			#Region 0 (0 --- q/4 and q/2 --- 3q/4)
			if (shared[i] >= q*0.125 and shared[i] < q*0.625):
				shared[i] = 1
			else:
				shared[i] = 0
		elif (u[i] == 1):
			#Region 1 (q/4 --- q/2 and 3q/4 --- q)
			if (shared[i] >= q*0.875 and shared[i] < q*0.375):
				shared[i] = 0
			else:
				shared[i] = 1
	return shared

# ----- SHARED VALUES -----
n = 1024 #15
q_exp = n
if n>50:
	q_exp = 50 # n is too big for computation
q = 2**q_exp-1 # 2^n-1

xN_1 = np.array([1] + [0] * (n-1) + [1]) # (x^n + 1)


# ----- ALICE -----
A = np.floor(np.random.random(size=(n))*q)%q
A = np.floor(p.polydiv(A,xN_1)[1])

sA = gen_poly(n,q)
eA = gen_poly(n,q)

bA = p.polymul(A,sA)%q
bA = np.floor(p.polydiv(sA,xN_1)[1])
bA = p.polyadd(bA,eA)%q

# ----- BOB -----
sB = gen_poly(n,q)
eB = gen_poly(n,q)

bB = p.polymul(A,sB)%q
bB = np.floor(p.polydiv(sB,xN_1)[1])
bB = p.polyadd(bB,eB)%q

u = np.array([0] * n)
for i in range(n-1):
	if (int(bB[i]/(q/4)) == 0): u[i] = 0
	elif (int(bB[i]/(q/2)) == 0): u[i] = 1
	elif (int(bB[i]/(3*q/4)) == 0): u[i] = 0
	elif (int(bB[i]/(q)) == 0): u[i] = 1

# ----- SHARED SECRETS -----
#Alice
sharedAlice = np.floor(p.polymul(sA,bB)%q)
sharedAlice = np.floor(p.polydiv(sharedAlice,xN_1)[1])%q  

#Bob
sharedBob = np.floor(p.polymul(sB,bA)%q)
sharedBob = np.floor(p.polydiv(sharedBob,xN_1)[1])%q

# ----- REMOVE ERROR -----
sharedAlice = extractError(sharedAlice)
sharedBob = extractError(sharedBob)

print("----- Shared values -----")
print(f" n: {n}")
print(f" q (2^{q_exp}-1): {q}")
print(f" xN_1: {len(xN_1)} | {xN_1}")
print(f" A: {len(A)} | {A}")

print("\n--------- Alice ---------")
print(f" s: {len(sA)} | {sA}")
print(f" e: {len(eA)} | {eA}")
print(f" b: {len(bA)} | {bA}")

print("\n---------- Bob ----------")
print(f" e: {len(sB)} | {sB}")
print(f" e: {len(eB)} | {eB}")
print(f" b: {len(bB)} | {bB}")
print(f" u: {len(u)} | {u}")

print("\n----- Shared secret -----")
print(f" Shared Secret Alice: {len(sharedAlice)} | {sharedAlice}")
print(f" Shared Secret Bob:   {len(sharedBob)} | {sharedBob}")

print("\n\n----- Verification -----")
err = 0
for i in range(len(sharedBob)):
	if (sharedAlice[i] != sharedBob[i]):
		print(f" Error at index: {i}")
		err +=1
if err == 0:
	print(" Everything correct!")