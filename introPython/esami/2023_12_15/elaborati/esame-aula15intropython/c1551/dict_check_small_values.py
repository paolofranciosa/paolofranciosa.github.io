def dict_check_small_values(d,threshold):
    if not isinstance(d,dict):
        raise TypeError
    i=0
    for value in d.values():
        if value>=threshold:
            i+=1
    if i==0:
        return True
    else:
        return False
        
    
    