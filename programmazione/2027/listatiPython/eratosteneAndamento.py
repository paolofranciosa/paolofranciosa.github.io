'''calcola la somma dei numeri primi minori di n e ne stampa la somma dei
reciproci, insieme al valore log log n'''
from math import sqrt,log

def compatta(lista):
#    return [x for x in numeri if x] # versione concisa
    comp = []
    for e in lista:
        if e != 0:
            comp.append(e)
    return comp

def crivello_eratostene(n):
    if n < 3:
        return []
    if n == 3:
        return [2]
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

def somma_rec_primi(n):
    primi = crivello_eratostene(n)
    somma = 0
    for i in range(len(primi)-1, -1, -1):
        somma += 1 / primi[i]
    return somma

if __name__ == "__main__":
    print(f'{"n":^12s} {"somma":^12s} {"loglog n":^12s} {"somma/loglog":^12s} {"log n":^12s} {"armonica":^12s} {"arm - log":^12s}')
    n = 4
    while n < 140000000:
        somma = somma_rec_primi(n)
        loglog = log(log(n))
        somma_inversi = sum((1/k for k in range(n-1, 0, -1)))
        print(f'{n:12d} {somma:12.7f} {loglog:12.7f} {somma/loglog:12.7f} {log(n):12.7f} {somma_inversi:12.7f} {somma_inversi - log(n):12.7f}')
        n *= 2