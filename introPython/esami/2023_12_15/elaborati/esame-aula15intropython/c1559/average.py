def average(L):
    somma = 0
    for i in range(len(L)):
        somma = somma + L[i]
    return somma/len(L)    

lista = [1,2,4,6]
print(average(lista))