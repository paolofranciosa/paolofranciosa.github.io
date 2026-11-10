'''viene mostrato l'uso della libreria matplotlib per la
visualizzazione di grafici.
Sono mostrate alcune delle funzioni principali,
ed alcuni dei loro parametri
'''

import matplotlib.pyplot as plt
import random
import math

# def random_sequence(n, val_inizio, val_fine, oscill):
#     '''restituisce una sequenza random generata
# aggiungendo un valore casuale in un intervallo oscill
# centrato su 0 sommato a una retta da val_inizio a val_fine'''
#     seq = [val_inizio + (val_fine - val_inizio) * (i / n) + \
#            oscill * random.random()-oscill/2 \
#            for i in range(n)]
#     return seq

def random_sequence_sin(n, val_base, oscill):
    '''restituisce una sequenza random generata
aggiungendo un valore casuale in un intervallo oscill
centrato su 0 sommato a una sinusoide'''
    seq = [val_base + math.sin(i / n * 4 * math.pi) * oscill + \
           oscill * 2 * random.random()-oscill \
           for i in range(n)]
    return seq

# complessita' O(n)
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
    n = int(input("Quanti punti nel periodo (sugg. 200)?: "))
    seq = random_sequence_sin(n, 40, 10)
    
    # crea oggetti grafici
    fig, ax = plt.subplots()
    # estremi asse y: da 0 a leggermente piu' del massimo valore
    ax.set_ylim(bottom = 0, top = max(seq) * 1.05)
    
    # disegna i valori, grafico a dispersione
    ax.scatter(range(n), seq, s = 4, label = "values") # s e' la dimensione dei punti, label associa una legenda alla serie

    # calcola due serie di medie mobili
    k1 = int(input("lunghezza finestra prima media mobile (sugg. 10)?: "))
    k2 = int(input(f"lunghezza finestra seconda media mobile (sugg. {4*k1})?: "))
    m_mob_1 = medie_mobili(seq, k1)
    m_mob_2 = medie_mobili(seq, k2)
    
    # disegna le due medie mobili sullo stesso grafico usato per i valori 
    # le sequenze range(k1-1)  e   m_mob_1  hanno la stessa lunghezza
    ax.plot(range(k1-1, n), m_mob_1, color = "red", linewidth=2, label = f'{k1}-mov_avg') # label associa una legenda alla serie
    # le sequenze range(k2-1)  e   m_mob_2  hanno la stessa lunghezza
    ax.plot(range(k2-1, n), m_mob_2, color = "green", linewidth=3, linestyle = "dashed", label = f'{k2}-mov_avg') # label associa una legenda alla serie

    ax.legend() # mostra le legende (label associate alle serie disegnate)
    plt.xlabel("time") # etichetta asse x
    plt.ylabel("ACME (dollars)") # etichetta asse y
    plt.show()
