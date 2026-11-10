def change_mins_in_zero(values):
    s=min(values)
    for i in range(len(values)):
        if values[i]==s:
            values[i]=0
            
        
    return values
        
