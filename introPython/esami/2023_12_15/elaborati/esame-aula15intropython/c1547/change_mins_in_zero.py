def change_mins_in_zero(values):
    if not isinstance(values,list):
        raise TypeError
    if len(values)==0:
        raise ValueError
    for i in values:
        if not isinstance(i,(int,float)):
            raise ValueError
    c=min(values)
    for i in range(len(values)):
        if values[i]==c:
            values[i]=0
    return values

