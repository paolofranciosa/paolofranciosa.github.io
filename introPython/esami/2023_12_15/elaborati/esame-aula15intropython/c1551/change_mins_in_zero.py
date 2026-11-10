def change_mins_in_zero(values):
    if not isinstance (values,list):
        raise TypeError
    
    minimo=values[0]
    for i in range(len(values)):
        if values[i]<minimo:
            minimo=values[i]
    for i in range(len(values)):
        if values[i]==minimo:
            values[i] = 0
    
    return values



    



    