# Scrivere un programma che legge da tastiera due numeri interi a e b
# e stampa 4 numeri interi casuali nell'intervallo [a, b].
import random

a = int(input("dammi l'estremo inferiore: "))
b = int(input("dammi l'estremo superiore: "))
valore = random.random() * (b-a) + a
print(valore)