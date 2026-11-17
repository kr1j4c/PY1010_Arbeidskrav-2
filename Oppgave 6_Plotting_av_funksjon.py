# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:29:04 2026

@author: krist
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200)

y = -x**2 - 5

plt.plot(x, y)

plt.title("f(x) = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()

plt.show()