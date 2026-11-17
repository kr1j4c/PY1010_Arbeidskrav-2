# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:57:13 2026

@author: krist
"""

import numpy as np

def grad_til_radian(v_grad):
    v_rad = v_grad * np.pi / 180
    return v_rad

v_grad = float(input("Skriv inn gradtallet: "))

v_rad = grad_til_radian(v_grad)

print("Vinkelen i radianer er:", v_rad)