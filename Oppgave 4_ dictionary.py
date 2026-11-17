# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:01:02 2026

@author: krist
"""

data = {
    "Norge": ["Oslo", 0.697],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }



land = input("Skriv inn et land: ")

hovedstad = data[land][0]
innbyggere = data[land][1]

print(hovedstad, "er hovedstaden i", land, "og det er",
    innbyggere, "mill. innbyggere i", hovedstad)



nytt_land = input("Skriv inn nytt land: ")
ny_hovedstad = input("Skriv inn hovedstad: ")
antall_innbyggere = float(input("Skriv inn antall innbyggere (i millioner): "))

data[nytt_land] = [ny_hovedstad, antall_innbyggere]

print(data)