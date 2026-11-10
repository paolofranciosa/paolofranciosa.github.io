def change_mins_in_zero(values):
    min= values[0]
    if len(values)>0:
        for i in range(len(values)):
            if values[i]<min:
                values[i]==0
        if min==values[0]:
            values[0]=0
    return values
