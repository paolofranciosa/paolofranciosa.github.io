'''stampa i numeri primi minori di n'''
def compatta(lista):
    comp = []
    for e in lista:
        if e != 0:
            comp.append(e)
    return comp

def crivello_eratostene(n):
    numeri = list(range(n)) # crea la list [0,1,2,3,4,...,n-2,n-1]
    # numeri[i] sara' impostato a 0 se i non e' primo
    numeri[1] = 0 # per definizione, 1 non e' primo
    div = 2
    while div*div < n:
        if numeri[div] != 0:
            for i in range(div*2, n, div):  # elimina i multipli di div
                numeri[i] = 0
        div += 1
    primi = compatta(numeri)
    return primi

if __name__ == "__main__":
    n = 1000
    primi = crivello_eratostene(n)
    print(primi)