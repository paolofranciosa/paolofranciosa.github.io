def dict_check_small_values(d, threshold):
    for k in d:
        if d[k] >= threshold:
            return False
            
        else:
            continue
    return True
        
        
