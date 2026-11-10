def dict_check_small_values(d, threshold):
    res = True
    for key in d:
        if d[key] >= threshold:
            res = False
    return res
        