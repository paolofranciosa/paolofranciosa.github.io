# Contare quanti dei quattro numeri sono maggiori o uguali a 0.6
# e visualizzare il risultato

import random

a = random.random()
b = random.random()
c = random.random()
d = random.random()
print(a, b, c, d)
contatore = 0
if a >= 0.6:
    contatore = contatore + 1
if b >= 0.6:
    contatore = contatore + 1
if c >= 0.6:
    contatore = contatore + 1
if d >= 0.6:
    contatore = contatore + 1
if contatore == 1:
    print("c'è un solo numero maggiore o uguale a 0.6")
else:
    print("ci sono", contatore, "numeri maggiori o uguali a 0.6")