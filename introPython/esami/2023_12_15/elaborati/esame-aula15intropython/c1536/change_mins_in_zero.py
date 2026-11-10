def change_mins_in_zero(values):
    tempmin = values[0]
    for ele in values:
        if ele < tempmin:
            tempmin = ele
    for i in range(len(values)):
        if values[i] == tempmin:
            values[i] = 0
