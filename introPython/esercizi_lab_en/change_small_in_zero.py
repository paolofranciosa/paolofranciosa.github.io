def change_small_to_zero(valori):
    media = sum(valori)/len(valori)
    for i in range(0,len(valori)):
        if valori[i] < media:
            valori[i] = 0
