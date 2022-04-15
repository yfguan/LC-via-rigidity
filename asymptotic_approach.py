# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 03:42:34 2022

@author: guanyunfeng
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

def H(x):
    return entropy([x, 1-x], base=2)

def Hm(x):
    return H(x) if x < 1/2 else 1

def T(x):
    return H(x) + np.log2(3) * (1-x)

# c = 1.974

# X = np.linspace(0, 1, 10000)
# Y = np.array([T(x) for x in X])
# plt.plot(X, Y)
# S = X[Y > c]
# (s1, s2) = (min(S), max(S))
# plt.plot([s1, s1], [0, T(s1)], 'k--')
# plt.plot([s2, s2], [0, T(s2)], 'k--')
# print('s2-s1 =', s2-s1)
# print((1+c)/2, 1-(s2-s1)+H(s2-s1))

# plt.figure()
# plt.plot(X, (3-X)/2)
# plt.plot(X, [1+H(x) for x in X])

#%%
# plt.figure()

# e = 0
# s1 += e
# s2 += e
# L = X[X > s2]

# plt.plot(L, [0.5 * (1 - s + s * Hm(s1/s)) + H(s) for s in L])
# plt.plot(L, [0.5 * (1 - s + s * Hm(1-s2/s)) + H(s) for s in L])
# print(max([0.5 * (1 - s + s * Hm(s1/s)) + H(s) for s in L]),
#       max([0.5 * (1 - s + s * Hm(1-s2/s)) + H(s) for s in L]))

#%%
# Approximate |x \oplus y| via even/odd partition
# c = 0.956
# X = np.linspace(0, 1, 50000)
# Y = np.array([H(x) for x in X])
# plt.plot(X, Y)
# S = X[Y > c]
# (s1, s2) = (min(S), max(S))
# plt.plot([s1, s1], [0, H(s1)], 'k--')
# plt.plot([s2, s2], [0, H(s2)], 'k--')
# print('s2-s1 =', s2-s1)
# print(1+c/2, 1-(s2-s1)/4+H((s2-s1)/2))

#%%
# Approximate |x \oplus y| 1) even/odd 2) |x| < n/2 / |x| > n/2
# c = 0.953
# X = np.linspace(0, 1, 10000)
# Y = np.array([H(x) for x in X])
# plt.plot(X, Y)
# S = X[Y > c]
# (s1, s2) = (min(S), max(S))
# plt.plot([s1, s1], [0, H(s1)], 'k--')
# plt.plot([s2, s2], [0, H(s2)], 'k--')
# print('s2-s1 = ', s2-s1)
# r = s2-s1

#%%
# Approximate |x \oplus y| |x| < n/2 / |x| > n/2
# c = 1.96

# X = np.linspace(0, 1, 10000)
# Y = np.array([T(x) for x in X])
# plt.plot(X, Y)
# S = X[Y > c]
# (s1, s2) = (min(S), max(S))
# plt.plot([s1, s1], [0, T(s1)], 'k--')
# plt.plot([s2, s2], [0, T(s2)], 'k--')
# print('s2-s1 =', s2-s1)
# r = s2-s1
# print((1+c)/2, (1-r)*H((0.5-r)/(1-r))+H(r))

#%%
# Approximate via hybrid method
c = 0.95

n = 12
N = 2**n
rig = (1792 + 64)*(64 + 64)
X = np.linspace(0, 1, 10000)
Y = np.array([H(x) for x in X])
plt.plot(X, Y)
S = X[Y > c]
(s1, s2) = (min(S), max(S))
plt.plot([s1, s1], [0, H(s1)], 'k--')
plt.plot([s2, s2], [0, H(s2)], 'k--')
print('s2-s1 =', s2-s1)
print(1.5 + 1/(2*n)*(c-1), 1+rig/n*H((s2-s1)/rig))
