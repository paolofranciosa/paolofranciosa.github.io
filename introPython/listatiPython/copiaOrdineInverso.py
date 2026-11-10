def copia_inversa(l):
    '''restituisce una copia della lista l in ordine inverso'''
    lista_nuova = []
    i = len(l) - 1
    while i >= 0:
        lista_nuova.append(l[i])
        i -= 1
    return lista_nuova


'''legge da tastiera una sequenza di numeri terminata da 0 e la stampa in ordine inverso'''
lista_numeri = []
num = int(input("scrivi un numero: "))
while num != 0:
    lista_numeri.append(num)
    num = int(input("scrivi un numero: "))
print(lista_numeri)
lista_bis = copia_inversa(lista_numeri)
print(lista_bis)
