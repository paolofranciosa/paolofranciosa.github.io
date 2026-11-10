def change_mins_in_zero(values):
    if not isinstance(values,list):
        raise TypeError
    if len(values)==0:
        return None
    minimo=min(values)
    for i in range(len(values)):
        if values[i]==minimo:
            values[i]=0
    return values

