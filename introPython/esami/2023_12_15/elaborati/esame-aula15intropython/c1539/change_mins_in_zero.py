def change_mins_in_zero(values):
    
    minimo=values[0]
    for i in range(len(values)):
        if values[i]<=minimo:
            minimo=values[i]
        if values[i]== minimo:
            values[i]=0
    return values

s=change_mins_in_zero([1,3,4,5,1,7,4,3])
print(s)
    