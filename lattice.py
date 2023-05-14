import matplotlib.pyplot as plt
import numpy as np

def getPoints(A, B, r):
    xval=[0]
    yval=[0]
    for a in range(-r, r):
        for b in range(-r, r):
            xnew=a*A[0] + b*B[0]
            xval.append(xnew)
            ynew=a*A[1] + b*B[1]
            yval.append(ynew)
    
    return xval,yval

P0 = (0, 0)
P1 = (3, 2)
P2 = (2, 7)
e = (-0.5, 0.7)

xval, yval=getPoints(P1, P2, 7)    

plt.xlabel('x')
plt.ylabel('y')
plt.axis([0,max(xval)/2,0,max(yval)/2])

plt.scatter(xval,yval)

# v1
x = np.array([P0[0], P1[0]])
y = np.array([P0[1], P1[1]])
plt.plot(x, y, color="orange", label="v1")

# v2
x = np.array([P0[0], P2[0]])
y = np.array([P0[1], P2[1]])
plt.plot(x, y, color="red", label="v2")

# v1 + v2
x = np.array([P0[0], P1[0] + P2[0]])
y = np.array([P0[1], P1[1] + P2[1]])
plt.plot(x, y, color="yellow", label="v1+v2")

# e 
x = np.array([P1[0] + P2[0], P1[0] + P2[0] + e[0]])
y = np.array([P1[1] + P2[1], P1[1] + P2[1] + e[1]])
plt.plot(x, y, color="green", label="e")
plt.plot(x, y, 'o', color="green")

# v1 + v2 + e 
x = np.array([P0[0], P1[0] + P2[0] + e[0]])
y = np.array([P0[1], P1[1] + P2[1] + e[1]])
plt.plot(x, y, color="purple", label="v1+v2+e")

plt.legend(loc="upper right")
plt.show()
