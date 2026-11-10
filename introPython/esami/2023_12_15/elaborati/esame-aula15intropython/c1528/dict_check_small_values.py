def dict_check_small_values(d,threshold):
    small = True
    for key in d:
        if d[key] >= threshold:
            small = False
    return small

