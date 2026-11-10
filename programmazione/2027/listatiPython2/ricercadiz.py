import random

def lista_casuale(n):
    l = []
    for i in range(n):
        l.append(random.randint(0,100000000))
    return l

def dizionario_casuale(n):
    d = {}
    for i in range(n):
        x = random.randint(0,100000000)
        d[x] = 44
    return d

def ricerca_in_lista(l, v):
    for i in range(len(l)):
        if l[i] == v:
            return i
    return None
