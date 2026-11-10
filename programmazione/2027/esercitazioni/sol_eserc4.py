import random

n = int(input("quanti valori vuoi generare? "))
conta = 0
somma = 0
massimo = -1 # sicuramente minore di tutti i valori generati
minimo = 2 # sicuramente maggiore di tutti i valori generati
esiste_elemento = False # diventa True se troviamo un elemento in (0.4, 0.5)
crescente = True # diventa False se troviano una coppia nell'ordine non corretto
numero_seq_crescenti = 0
while conta < n:
    x = random.random()
    print(x)
    if x > massimo:
        massimo = x
    if x < minimo:
        minimo = x
    if 0.4 < x and x < 0.5:
        esiste_elemento = True

    if conta > 0: # il test seguente non ha senso per il primo elemento generato
        if prec >= x: # sequenza non crescente
            crescente = False
            numero_seq_crescenti += 1
    prec = x # salva x per la prossima iterazione
    conta = conta + 1
numero_seq_crescenti += 1 # per tener conto dell'ultima sequenza
print("la somma è", somma)
print("il massimo è", massimo)
print("il minimo è", minimo)
if esiste_elemento:
    print("esiste almeno un elemento in (0.4, 0.5)")
else:
    print("non esiste nessun elemento in (0.4, 0.5)")
if crescente:
    print("sequenza crescente")
else:
    print("sequenza non crescente")
print("il numero di sequenze crescenti è", numero_seq_crescenti)
 