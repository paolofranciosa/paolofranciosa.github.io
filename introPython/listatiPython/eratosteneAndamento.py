'''calcola la somma dei numeri primi minori di n e ne stampa la somma dei
reciproci, insieme al valore log log n'''
from math import sqrt,log

def compatta(lista):
    comp = []
    for e in lista:
        if e != 0:
            comp.append(e)
    return comp

def crivello_eratostene(n):
    numeri = list(range(n)) # crea la list [0,1,2,3,4,...,n-2,n-1]
    numeri[1] = 0
    max_div = int(sqrt(n))+1
    for div in range(2, max_div+1):
        if numeri[div] != 0:
            for i in range(2*div, n, div):
                numeri[i] = 0
    primi = compatta(numeri)
    return primi

def crivello_eratostene_bis(n): # modificato range del for interno
    numeri = list(range(n)) # crea la list [0,1,2,3,4,...,n-2,n-1]
    numeri[1] = 0
    div = 2
    while div*div < n:
        if numeri[div] != 0:
            for i in range(div*div, n, div):
                numeri[i] = 0
        div += 1
    primi = compatta(numeri)
    return primi

if __name__ == "__main__":
    print(f'{"n":^12s} {"somma":^12s} {"loglog n":^12s} {"somma/loglog":^12s}')
    n = 4
    while n < 140000000:
        primi = crivello_eratostene(n)
        somma = 0
        for i in range(len(primi)-1, -1, -1):
            somma += 1 / primi[i]
            loglog = log(log(n))
        print(f'{n:12d} {somma:12.7f} {loglog:12.7f} {somma/loglog:12.7f}')
        n *= 2