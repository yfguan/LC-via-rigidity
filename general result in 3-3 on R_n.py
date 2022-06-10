import numpy as np

gamma = np.log(9/4) 

X = np.array([[1, 4], [3, 1], [1, 1], [1, 1]]).T
Z = np.log(X[0] / X[1])
G = np.max(np.abs(Z))
pi = (X[0] * X[1]) ** 0.5
pi = pi/np.sum(pi)
EZ = np.sum(Z * pi)

print(EZ)
print(gamma / (6*G) * (-4 * EZ) / (EZ + G))
print(np.log(6/(4 + 3**0.5)))