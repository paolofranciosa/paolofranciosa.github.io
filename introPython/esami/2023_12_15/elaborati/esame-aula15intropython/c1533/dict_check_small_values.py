def dict_check_small_values(d, threshold):
    for i in d:
        if d[i]>=threshold:
            return False
    return True