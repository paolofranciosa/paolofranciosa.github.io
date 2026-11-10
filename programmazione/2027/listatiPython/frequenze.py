'''generare un dizionario che associa a ciascuna
lettera  minuscola un intero casuale in [0,10]'''
import random

def freq_casuali_lettere():
    f = {}
    for lettera in range('a','z'):
        f[lettera] = random.randint(0,10)   
    return f
