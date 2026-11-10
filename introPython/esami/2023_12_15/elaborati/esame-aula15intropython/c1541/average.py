def average(L):
    tot=0
    for i in range(len(L)):
        tot+=L[i]
        average=tot/(len(L))
    return average

L=[1,2.4,3.7,9,11,0]
print(average(L))
    