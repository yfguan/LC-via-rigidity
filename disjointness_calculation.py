# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:40:50 2022

@author: guanyunfeng
"""

import numpy as np

P = np.array(
    [[8, 1], [1, 7], [1, 3], [1, 3], [1, 3], [1, 1], [1, 1], [1, 1]]).T

Z = np.log(P[0] / P[1])

pi = (P[0] * P[1]) ** 0.5
pi = pi / np.sum(pi)

EZ = np.sum(Z * pi)

G = np.log(8)

alpha1 = np.log(np.sum((P[0] * P[1]) ** 0.5))
alpha2 = np.log((27 * 8) ** 0.5)

beta = np.log(27/8) / (6 * G) * min([1, -4*EZ / (EZ + G)])