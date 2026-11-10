def average(L):
    n=len(L)
    somma=0
    for i in range(len(L)):
        somma+=L[i]
        media=somma/n
    return media
s=average([1,2,3])
print(s)
s=average([3,6,8])
print(s)