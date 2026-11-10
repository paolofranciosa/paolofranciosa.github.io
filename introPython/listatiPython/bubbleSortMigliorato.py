def bubblesort(seq):
    end=len(seq)-1   # end indica dove termina la parte da ordinare.
                     # La prima scansione deve ordinare tutta la sequenza.
                     # Nelle successive scansioni ci si puo' fermare dove 
                     # e' stato eseguito l'ultimo scambio durante la scansione precedente.
    while end > 0:
        last_swap = 0       # per memorizzare la posizione dell'ultimo scambio
        for j in range(0,end):
            if seq[j] > seq[j+1]:
                last_swap = j
                seq[j], seq[j+1] = seq[j+1],seq[j]
        end = last_swap     # la prossima scansione ordinera' solo fino alla 
                            # posizione dell'ultimo scambio