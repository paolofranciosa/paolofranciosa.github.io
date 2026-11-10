def change_mins_in_zero(values) :
    minimo = min(values)
    a = 0
    while a < len(values) :
        if values[a] == minimo :
            values[a] = 0
        a+=1
    return
        