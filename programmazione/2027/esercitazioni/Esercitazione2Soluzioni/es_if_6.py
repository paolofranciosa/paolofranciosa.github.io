# Visualizzare il massimo tra i quattro valori

import random

a = random.random()
b = random.random()
c = random.random()
d = random.random()
print(a, b, c, d)
massimo = a
if b > massimo:
    massimo = b
if c > massimo:
    massimo = c
if d > massimo:
    massimo = d
print("il massimo è", massimo)
