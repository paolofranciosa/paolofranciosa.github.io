def change_mins_in_zero(values):
    m = min(values)
    i = 0
    while i < len(values):
        if values[i] == m:
            values[i] = 0
            i += 1
        else:
            i += 1
    return values
print(change_mins_in_zero([3,10,40,40,6,2]))