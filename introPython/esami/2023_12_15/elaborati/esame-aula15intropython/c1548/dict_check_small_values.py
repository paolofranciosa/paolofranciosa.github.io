def dict_check_small_values(d, threshold):
    if not isinstance(d,dict):
        raise TypeError
    if not isinstance(threshold,(int,float)):
        raise TypeError
    for x in d:
        if not isinstance(d[x],(int,float)):
            raise TypeError
    for x in d:
        if d[x]>=threshold:
            return False    
    return True
                