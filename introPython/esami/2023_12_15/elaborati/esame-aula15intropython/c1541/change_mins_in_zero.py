def change_mins_in_zero(values):
    v=values
    mi=v[0]
    for i in range(len(v)):
        if v[i]<=mi:
            mi=v[i]
    for i in range(len(v)):
        if v[i]==mi:
            v[i]=0
    return v

v=[4,3,2,1,4,5,6]
print(change_mins_in_zero(v))
b=[9,0,3,1,-3,-3,2]
print(change_mins_in_zero(b))