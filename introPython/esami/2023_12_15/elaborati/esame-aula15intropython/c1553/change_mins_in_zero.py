def change_mins_in_zero(values):
    minimo=10
    for i in range(len(values)):
        if values[i]<=minimo:
            minimo=values[i]
            values[i]=0
    return values