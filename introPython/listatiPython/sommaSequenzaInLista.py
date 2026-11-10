def somma_sequenza(l):
    '''restituisce la somma degli elementi nella lista, assumendo che siano tutti numerici'''
    somma = 0
    for v in l:
        somma += v
    return somma


'''legge da tastiera una sequenza di numeri terminata da 0 e ne stampa la somma'''
lista_numeri = []
num = int(input("scrivi un numero: "))
while num != 0:
    lista_numeri.append(num)
    num = int(input("scrivi un numero: "))
print(lista_numeri)
print(somma_sequenza(lista_numeri))

