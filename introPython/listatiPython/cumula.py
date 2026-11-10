def cumulata(l):
    '''restituisce una lista che contiene la sequenza l cumulata'''
    cumulata = list(l) # crea una copia di l
    for i in range(1, len(l)):
        cumulata[i] = cumulata[i-1] + l[i]
    return cumulata


''' legge una sequenza di valori da tastiera terminata da 0,
la memorizza in una lista,
e stampa la sequenza cumulata'''

lista_numeri = []
num = int(input("scrivi un numero: "))
while num != 0:
    lista_numeri.append(num)
    num = int(input("scrivi un numero: "))
cum = cumulata(lista_numeri)
print("---------|---------")
print("  freq   | cumulate")
print("---------|---------")
for i in range(len(lista_numeri)):
    print("%5d    |%5d" % (lista_numeri[i], cum[i]))

