def dict_check_small_values(d, threshold):
    d={}
    if not isinstance (d.values,(int, float)):
        raise TypeError
    if not isinstance (threshold,(int, float)):
        raise TypeError
    return all(d.values< threshold for values in d.values())

