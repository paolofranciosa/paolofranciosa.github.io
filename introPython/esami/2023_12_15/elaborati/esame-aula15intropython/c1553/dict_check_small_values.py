def dict_check_small_values(d,threshold):
    for k in d.values():
        if k >= threshold:
            return False
    return True