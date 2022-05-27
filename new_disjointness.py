
import numpy as np
import matplotlib.pyplot as plt
from math import gcd

def reduce(t):
    a, b = t[0], t[1]
    return (a//gcd(a, b), b//gcd(a, b))

L = [(1, 1)]

T = 40
r = 100000000000

def goodgrow(l):
    if l[0]/l[1] < 1/r:
        E = [(4, 1), (2, 1), (2, 1), (1, 1)]
    elif l[0]/l[1] < 1:
        E = [(4, 1), (1, 3), (1, 1), (1, 1)]
    elif l[0]/l[1] < r:
        E = [(1, 4), (3, 1), (1, 1), (1, 1)]
    else:
        E = [(1, 4), (1, 2), (1, 2), (1, 1)]
    return [(l[0]*e[0], l[1]*e[1]) for e in E]

def badgrow(l):
    if l[0]/l[1] < 1:
        E = [(1, 4), (3, 1), (1, 1), (1, 1)]
    else:
        E = [(1, 4), (1, 2), (1, 2), (1, 1)]
    return [(l[0]*e[0], l[1]*e[1]) for e in E]

def posgoodgrow(l):
    if l[0]/l[1] < 1/r:
        E = [(4, 1), (2, 1), (2, 1), (1, 1)]
    elif l[0]/l[1] < 1:
        E = [(4, 1), (1, 3), (1, 1), (1, 1)]
    elif l[0]/l[1] < r:
        E = [(1, 4), (3, 1), (1, 1), (1, 1)]
    else:
        E = [(1, 4), (1, 2), (1, 2), (1, 1)]
    return [(l[0]*e[0], l[1]*e[1]) for e in E]

grow = goodgrow

for epoch in range(T):
    newL = []
    for l in L:
        newL.extend([reduce(t) for t in grow(l)])
    L = list(set(newL))

mem = dict()
ratio = [l[0] / l[1] for l in L]
def NN(t, L):
    t = reduce(t)
    if t in mem.keys():
        return mem[t]
    optN = 0
    for i in range(len(L)):
        opt = L[optN]
        if abs(ratio[i] - t[0]/t[1]) < abs(opt[0]/opt[1] - t[0]/t[1]):
            optN = i
    mem[t] = optN
    return optN

n = len(L)
A = np.zeros((n, n))
for i in range(n):
    l = L[i]
    for t in grow(l):
        nn = NN(t, L)
        A[nn, i] += max(t[0]/L[nn][0], t[1]/L[nn][1])
        
res = [np.linalg.norm(x) for x in np.linalg.eig(A)[0]]
res.sort()
print(res[-1])