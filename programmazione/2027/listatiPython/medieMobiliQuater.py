import matplotlib.pyplot as plt
import random
import math

def random_sequence(n, val_inizio, val_fine, oscill):
    '''restituisce una sequenza random generata
aggiungendo un valore casuale in un intervallo oscill
centrato su 0 sommato a una retta da val_inizio a val_fine'''
    seq = [val_inizio + (val_fine - val_inizio) * (i / n) + \
           oscill * random.random()-oscill/2 \
           for i in range(n)]
    return seq

def random_sequence_sin(n, val_base, oscill):
    '''restituisce una sequenza random generata
aggiungendo un valore casuale in un intervallo oscill
centrato su 0 sommato a una sinusoide'''
    seq = [val_base + math.sin(i / n * 4 * math.pi) * oscill + \
           oscill * random.random()-oscill/2 \
           for i in range(n)]
    return seq

# complessità O(n)
def medie_mobili(seq, k):
    somma = 0
    for i in range(k):
        somma += seq[i]
    medie = [somma/k]
    for inizio in range(0, len(seq)-k):
        # modificare somma
        somma -= seq[inizio]
        somma += seq[inizio+k]
        medie.append(somma/k)
    return medie
      
if __name__ == "__main__":
    print("Simuliamo una variabile con andamento sinusoidale e rumore random")
    n = int(input("Quanti punti nel periodo?: "))
    seq = random_sequence_sin(n, 20, 10)
    fig, ax = plt.subplots()
    ax.scatter(range(n), seq, s = 4) # s è la dimensione dei punti
    risp = input("Vuoi le medie mobili? (s/n): ").upper()
    if risp == "S":
        k1 = int(input("periodo media corta?: "))
        k2 = int(input(f"periodo media lunga (sugg. {4*k1})?: "))
        m_mob_1 = medie_mobili(seq, k1)
        m_mob_2 = medie_mobili(seq, k2)
        ax.plot(range(k1-1, n), m_mob_1, linewidth=2)
        ax.plot(range(k2-1, n), m_mob_2, linewidth=3, linestyle = "dashed")
    plt.show()
    plt.savefig("medie.pdf")