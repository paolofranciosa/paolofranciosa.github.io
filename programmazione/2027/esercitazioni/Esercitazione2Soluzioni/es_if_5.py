# Visualizzare tutti i valori minori della media

import random

a = random.random()
b = random.random()
c = random.random()
d = random.random()
print(a, b, c, d)
media = (a+b+c+d) / 4
if b < media:
    print(b)
if c < media:
    print(c)
if d < media:
    print(d)
