def average(L):
    somma = 0
    for el in L:
        somma = somma + el
    media = somma/len(L)
    return(media)
    

Lista = [1, 3, 6, 7, 8]

print(average(Lista))