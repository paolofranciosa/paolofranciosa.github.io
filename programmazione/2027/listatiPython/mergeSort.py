def merge(S,inizio, mid, fine):
    '''S contiene una sequenza crescente dalla posizione inizio alla posizione mid comprese,
    e una sequenza crescente dalla posizione mid+1 alla posizione fine comprese.
    Gli elementi di queste due sequenze vengono fusi in una sola sequenza crescente
    dalla posizione inizio alla posizione fine comprese'''
    
    i=inizio
    j=mid+1
    temp=[]
    
    # Parte 1 - Inserisci in testa il piu' piccolo fino a
    # esaurimento di una delle porzioni
    while i<=mid and j<=fine:
        if S[i]<=S[j]:
            temp.append(S[i])
            i += 1
        else:
            temp.append(S[j])
            j += 1
            
    # Parte 2 - Esattamente UNA sequenza e' esaurita.
    # Va aggiunta la coda residua di una delle due sequenze
    if i > mid:
        residuo = range(j, fine+1)
    else:
        residuo = range(i, mid+1)
    for k in residuo:
        temp.append(S[k])
        
    # Parte 3 - la lista temp deve essere copiata su S[inizio:fine+1]
    for k in range(len(temp)):
        S[inizio+k] = temp[k]

def mergesort(S, inizio=None, fine=None):
    '''realizza l'algoritmo di ordinamento per fusione'''
    if inizio == None:
        inizio = 0
        fine = len(S)-1
    if inizio < fine:
        mid=(inizio+fine)//2
        mergesort(S, inizio, mid)
        mergesort(S, mid+1, fine)
        merge(S, inizio, mid, fine)

elenco = [4, 2, 6, 5, 7, 9, 8, 4, 5, 1, 2, 0, 4]
print(elenco)
mergesort(elenco)
print(elenco)