def average(L):
    total = 0
    
    for i in range(len(L)):
        total += L[i]
        
    average = total / len(L)
    return average