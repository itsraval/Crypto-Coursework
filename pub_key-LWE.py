import numpy as np

n = 25
s = 72
q = 127

M = 0

A = np.random.randint(0, q+1, n)
e = np.random.randint(0, 5, n)

B = np.array([(A[i]*s+e[i])%q for i in range(n)])

print(f"\n---- Alice ----")
print(f"Message bit: \t\t{M}")
print(f"Public Key (A):\t\t{A}")
print(f"Public Key (B):\t\t{B}")
print(f"Error vector (e):\t{e}")
print(f"Secret key (s):\t\t{s}")
print(f"Prime number (q):\t{q}")

sample = np.random.randint(0, n, n//5)
u = 0
v = 0
for i in range(len(sample)):
	u += A[sample[i]]
	v += B[sample[i]]
u = u % q
v = (v + (int(q//2) * M)) % q

print(f"\n---- BoB ----")
print(f"Sample vector (sample):{sample})")
print(f"Cipher text (u):\t{u}")
print(f"Cipher text (v):\t{v}")

print(f"\n---- Alice ----")
res = (v - s*u) % q
if res>q/2:
	print(f"The message bit is a 1")
else:
	print(f"The message bit is a 0")