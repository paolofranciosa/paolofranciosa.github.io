# complessità O(n * k)

def calcola_media(seq, pos_iniz, pos_fin):
    '''restituisce la media degli elementi di seq da
pos_iniz (incluso) a pos_fin (escluso)'''
    somma = 0
    for i in range(pos_iniz, pos_fin):
        somma += seq[i]
    return somma/(pos_fin-pos_iniz)

def medie_mobili(s, k):
    '''crea e restituisce una lista contenente le medie mobili
di ordine k della sequenza s'''
    # tralascio le verifiche
    # assumo k <= len(s)  e  len(s) > 0,   k > 0
    medie = []  # conterrà le medie mobili
    # devo calcolare le medie da inizio (incluso) a inizio+k (escluso)
    # dove inizio vale 0, 1, 2, ..., len(s)-k incluso
    for inizio in range(len(s)-k+1):
        # calcolare la media da posiz inizio (inclusa) a inizio+k (esclusa)
        #                       sono esattamente k elementi
        medie.append(calcola_media(s, inizio, inizio+k))
    return medie


seq = [2, 4, 3, 6, 8, 9, 10, 12]  # len vale 8
k = 4   #inizio vale 0, 1, 2, 3, 4, 5 (è proprio 8-3),  5 compreso
m_mob = medie_mobili(seq, k)
print(m_mob)