def change_mins_in_zero(values):
    # lista in input
    minim = 100000000
    for i in range(len(values)):
        if values[i] < minim:
            minim=values[i]
    for i in range(len(values)):
        if (values[i] == minim):
            values.remove(values[i])
            values.insert(i, 0)
    return None
    
    

l =  [1,2,3,4]


print(change_mins_in_zero(l))