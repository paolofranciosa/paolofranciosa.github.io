def change_mins_in_zero(values):
    minimum=values[0]
    if type(values[0])==int or type(values[0])==float:
        for i in values:
            if type(i)!=int and type(i)!=float:
                raise TypeError
    if type(values[0])==str:
        for i in values:
            if type(i)!=str:
                raise TypeError
    for i in values:
        if i<minimum:
            minimum=i
    for i in range(len(values)):
        if values[i]==minimum:
            values[i]=0
    return values

