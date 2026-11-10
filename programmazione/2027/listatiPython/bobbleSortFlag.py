def bubblesort(seq):
    ordinato = False
    while not ordinato:
        ordinato = True
        for j in range(len(seq)-1):
            if seq[j] > seq[j+1]:
                ordinato = False
                seq[j], seq[j+1] = seq[j+1],seq[j]


l = [5, 3, 2, 6, 7, 5, 4, 7, 9, 1, 3]
print(l)
bubblesort(l)
print(l)