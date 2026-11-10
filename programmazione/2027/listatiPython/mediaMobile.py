def media_mobile(s, k):
    '''restituisce la sequenza delle medie di s su porzioni
di lunghezza k. La seq delle medie mobili sara' lunga
len(s) - k + 1.
Ciascuna media e' ottenuta da zero sommando tutti gli elementi nella finestra.'''
    medie = []
    for inizio in range(len(s)-k+1):  # ultimo valore di inizio e' len(s)-k
        # sommo da s[inizio] a s[inizio+k-1] inclusi
        tot = 0
        for p in range(inizio, inizio+k):
            tot += s[p]
        medie.append(tot/k)
    return medie

def media_mobile_veloce(s, k):
    '''restituisce la sequenza delle medie di s su porzioni
di lunghezza k. La seq delle medie mobili sara' lunga
len(s) - k + 1.
Ciascuna media e' ottenuta dalla precedente eliminando l'elemento uscente dalla finestra e
aggiungendo l'elemento entrante nella finestra.'''
    medie = []
    # calcolo la prima media, da [0] a [k-1]
    tot = 0
    for p in range(0, k):
            tot += s[p]
    medie.append(tot/k)
    # abbiamo ancora tot, somma degli elementi nella finestra
    # calcolo le successive in modo incrementale modificando tot
    for inizio in range(1, len(s)-k+1): # esce [inizio-1] ed entra [inizio+k-1]
        tot -= s[inizio-1]
        tot += s[inizio+k-1]
        medie.append(tot/k)
    return medie

a = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0]
print(media_mobile(a, 4))
print(media_mobile_veloce(a, 4))
