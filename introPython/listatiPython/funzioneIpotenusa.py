# definizione di una funzione che accetta due parametri che
# rappresentano le misure dei due cateti di un triangolo rettangolo e
# restituisce la misura dell'ipotenusa

import math

def calcola_ipotenusa(cat1, cat2):
    ipot = math.sqrt(cat1**2 + cat2**2)
    return ipot


# esempi di uso della funzione

a = int(input("Misura del primo cateto: "))
b = int(input("Misura del secondo cateto: "))
print("l'ipotenusa misura", calcola_ipotenusa(a, b))
