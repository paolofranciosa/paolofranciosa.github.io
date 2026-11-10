def calcola_media(s, inizio, fine):
    # CALCOLA E RESTITUISCE LA MEDIA DI UNA PORZIONE DI seq
                             # [inizio] incluso   [fine] escluso
    somma = 0
    for e in s[inizio:fine]: # e E' UN ELEMENTO DELLA LISTA
        somma = somma + e
    m = somma / (fine-inizio)
    return m


def medie_mobili(seq, k):
    n = len(seq)
    medie = []
#   FACENDO VARIARE IL PUNTO DI INIZIO (inizio) DA 0 A n-k compreso
    for inizio in range(n-k+1):
        # CALCOLARE LA MEDIA DEGLI ELEMENTI DA inizio A inizio+k (escluso)
        # APPENDERLA A medie
        nuovamedia = calcola_media(seq, inizio, inizio+k)
        medie.append(nuovamedia)
    return medie
    
print(medie_mobili([2, 3, 4, 5, 6, 7], 2))