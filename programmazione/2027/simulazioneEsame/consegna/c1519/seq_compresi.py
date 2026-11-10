def seq_compresi(L,low,high):
    '''restituisce il numero di valori
nella lista L che sono compresi tra low
e high(estremi inclusi). Puo assumere che
gli argomenti siano di tipo corretto,
cioè una lista di numeri e due numeri.'''
    n=0
    for i in range(len(L)//2):
        for e in range(len(L)-1):
            if L[i] == low:
                if L[e] == high:
                    n = e - i +1
    return n