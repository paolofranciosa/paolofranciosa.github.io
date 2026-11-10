def somma_lista(seq, inizio = None, fine = None):
    '''restituisce la somma degli elementi di seq a partire
dalla posizione inizio alla posizione fine (comprese)
se viene chiamata con un solo parametro gli estremi
inizio e fine vengono impostati a 0 e len(seq) - 1'''
    
    if fine is None:
        inizio = 0
        fine = len(seq) - 1

    if fine == inizio: # un solo elemento
        return seq[inizio]
    
    med = (inizio + fine) // 2
    prima_parte = somma_lista(seq, inizio, med)
    seconda_parte = somma_lista(seq, med + 1, fine)
    return prima_parte + seconda_parte
    
if __name__ == "__main__":
    print(somma_lista([3, 4, 3, 2, -1, 2, 6, 7, 10, -20]))
    