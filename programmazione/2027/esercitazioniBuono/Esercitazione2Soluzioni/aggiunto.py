# Visualizzare il valore più vicino a 0.5

import random

a = random.random()
b = random.random()
c = random.random()
d = random.random()
print(a, b, c, d)

miglior_valore = a
miglior_delta = abs(a-0.5)

if abs(b - 0.5) < miglior_delta:
    miglior_valore = b
    miglior_delta = abs(b - 0.5)
if abs(c - 0.5) < miglior_delta:
    miglior_valore = c
    miglior_delta = abs(c - 0.5)
if abs(d - 0.5) < miglior_delta:
    miglior_valore = d
    miglior_delta = abs(d - 0.5)
    
print("il più vicino a 0.5 è", miglior_valore)
