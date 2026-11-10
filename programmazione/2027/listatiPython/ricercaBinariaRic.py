def ricerca_binaria_ric(L, x, start, end):
    '''rstituisce la posizione di x nella lista ordinata L,
assumendo che tale posizione sia compresa tra start ed end inclusi.
Restituisce -1 se x non è presente in L'''
    if start > end:
        return -1
    mid = (start+end)//2
    if L[mid] < x:
        return ricerca_binaria_ric(L, x, mid+1, end)
    elif L[mid] > x:
        return ricerca_binaria_ric(L, x, start, mid-1)
    else:
        return mid

def ricerca_binaria(L, x):
    return ricerca_binaria_ric(L, x, 0, len(L)-1)

lista = [3, 5, 7, 12, 14, 20]
print(lista)
print(ricerca_binaria(lista, 3))
print(ricerca_binaria(lista, 5))
print(ricerca_binaria(lista, 7))
print(ricerca_binaria(lista, 12))
print(ricerca_binaria(lista, 14))
print(ricerca_binaria(lista, 20))
print(ricerca_binaria(lista, 1))
print(ricerca_binaria(lista, 8))
print(ricerca_binaria(lista, 30))
