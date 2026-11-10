def dict_check_small_values(d, threshold):
    smaller = True
    for k in d.values():
        if k >= threshold:
            smaller = False
    return smaller

d = {"Mario": 1000, "Gianna" : 8000, "Alberto": 4000}

print(dict_check_small_values(d, 9000))