def change_mins_in_zero(values):
    minimo = values[0]
    for i in range(len(values)):
        if values[i] < minimo:
            minimo = values[i]
    for i in range(len(values)):
        if values[i] == minimo:
            values[i] = 0
    return print(values)

lista = [1,4,52,25,214,1,3,5]

change_mins_in_zero(lista)