def change_mins_in_zero(values):
    minimum = values[0]
    for i in range(1,len(values)):
        if values[i] < minimum:
            minimum = values[i]
    for i in range(len(values)):
        if values[i] == minimum:
            values[i] = 0
    return
