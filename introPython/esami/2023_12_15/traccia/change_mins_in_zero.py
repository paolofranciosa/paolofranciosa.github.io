def change_mins_in_zero(valori):
    minimo = min(valori)
    for i in range(0,len(valori)):
        if valori[i] == minimo:
            valori[i] = 0
