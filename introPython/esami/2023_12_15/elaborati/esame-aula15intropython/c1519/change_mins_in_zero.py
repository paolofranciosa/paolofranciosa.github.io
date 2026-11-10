def change_mins_in_zero(values):
    conta=0
    if not isinstance (values, list):
        return (Error)
    if len(values)==0:
        return (Error)
    minimo=values[0]
    for i in range (1,len(values)):
        if values[i]<=minimo:
            minimo=values[i]
            values[i]=0
            conta+=1
    if minimo==values[0]:
        values[0]=0
    return(values)
print (change_mins_in_zero([3,6,3,4,6,5]))