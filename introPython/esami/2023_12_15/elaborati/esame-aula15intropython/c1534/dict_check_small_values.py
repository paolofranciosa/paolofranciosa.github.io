def dict_check_small_values(d, threshold):
    smaller = True
    for i in d:
        if d[i] >= threshold:
            smaller = False
    return smaller
    
    