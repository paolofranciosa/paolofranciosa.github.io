def dict_check_small_values(d, threshold):
    if not isinstance(d,dict):
       raise TypeError
    for k in d:
        if d[k] >= threshold:
            return False
    return True
