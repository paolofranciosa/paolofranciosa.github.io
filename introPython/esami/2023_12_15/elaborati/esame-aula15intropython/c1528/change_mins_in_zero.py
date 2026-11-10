def change_mins_in_zero(values):
    minimo = min(values)
    for i in range(len(values)):
        if values[i] == minimo:
            values[i] = 0
    return values
            
            