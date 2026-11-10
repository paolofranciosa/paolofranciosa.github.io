import random

n = int(input("quanti valori vuoi generare? "))
conta = 0
lungh_max = 0 # massima lunghezza di una sequenza crescente
lungh = 1 # lunghezza della sequenza crescente corrente
while conta < n:
    x = random.random()
    print(x)
    if conta > 0:
        if prec < x: # continua la seq crescente
            lungh += 1
        else: # termina la seq crescente
            if lungh > lungh_max: # se supero lunghezza massima corrente
                lungh_max = lungh 
            lungh = 1 # riparto con il conteggio per la nuova sequenza crescente
    prec = x
    conta = conta + 1
# consideriamo l'ultima sequenza crescente
if lungh > lungh_max:
    lungh_max = lungh
print("la lunghezza massima di una sequenza crescente è", lungh_max)