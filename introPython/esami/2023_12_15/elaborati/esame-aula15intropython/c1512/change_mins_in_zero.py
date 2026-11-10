def change_mins_in_zero(values):
    new_list = []
    for i in range(len(values)):
        if values[i-1] >= values[i]:
            new_list.append(0)
        else:
            new_list.append(values[i])
    return new_list
    print(new_list)
        
        
        