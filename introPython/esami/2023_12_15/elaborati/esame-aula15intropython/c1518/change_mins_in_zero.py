def change_mins_in_zero(values):
    k=min(values)
    for i in range(0,len(values)):
        if values[i]==k:
            values[i]=0

        