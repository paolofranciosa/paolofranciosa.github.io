def dict_check_small_values(d, threshold):
    if not isinstance(d,dict):
        raise TypeError
    if not isinstance(threshold,(int,float)):
        raise TypeError
    for i in d.values():
        if i>=threshold:
            return False
    return True


    