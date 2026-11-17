# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:11:02 2026

@author: krist
"""

import numpy as np

def beregn(a, b):

    # Areal trekant
    areal_trekant = (a * b) / 2

    # Halvsirkel
    r = a / 2

    areal_halvsirkel = 0.5 * np.pi * r**2

    areal = areal_trekant + areal_halvsirkel

    # Ytre omkrets
    hypotenus = np.sqrt(a**2 + b**2)

    omkrets = b + hypotenus + np.pi * r

    return areal, omkrets


a = float(input("Skriv inn a: "))
b = float(input("Skriv inn b: "))

areal, omkrets = beregn(a, b)

print("Areal =", areal)
print("Ytre omkrets =", omkrets)