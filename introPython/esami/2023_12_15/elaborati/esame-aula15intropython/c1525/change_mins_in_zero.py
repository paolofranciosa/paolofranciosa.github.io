def change_mins_in_zero(v):
    if len (v)==0:
        raise ValueError
    minim=v[0]
    for i in range(len(v)):
        if v[i] < minim:
            minim=v[i]
    for j in range (len(v)):
        if v[j]==minim:
            v[j]=0
    return v
print(change_mins_in_zero([2,1,3,1,5]))