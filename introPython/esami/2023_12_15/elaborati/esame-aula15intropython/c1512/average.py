def average(L):
    if isinstance (L, list):
        summ = 0
        for i in range(len(L)):
            summ = L[i] + summ
        result = summ / len(L)
        return result
    else:
        raise TypeError
    
    
