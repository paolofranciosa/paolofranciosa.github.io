def average(L):
    som = 0
    average = 0
    for i in range(len(L)):
        som = som + L[i]
        average = som/(i+1)
        
    return average
        
        


lista = [5,6,9,4,22,11]

print(average(lista))
        
                   
        