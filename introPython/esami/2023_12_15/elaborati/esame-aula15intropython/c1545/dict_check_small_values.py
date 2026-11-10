def dict_check_small_values(d,threshold):
    for key in d:
        if d[key]>=threshold:
            return False
    return True

d = {"Mario": 1000, "Gianna" : 80000, "Alberto": 4000}

