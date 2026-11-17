# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:51:39 2026

@author: krist
"""

import math

antall_elever = int(input("Skriv inn antall elever: "))

pizzaer = math.ceil(antall_elever / 4)

print("Det må handles inn", pizzaer, "pizzaer til festen.")