def average(L):
    for i in range(len(L)):
        if not isinstance(L[i], (int, float)):
            raise TypeError
        tot_sum= sum(L)
        mean= tot_sum/len(L)
        return mean
L=[1,4,6,9]
print(average(L))
    

    