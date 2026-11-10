def dict_check_small_values(d, threshold):
    for key in d:
        if d[key] >= threshold:
            return False
    
    return
d = {"Mario": 1000, "Gianna" : 8000, "Alberto": 4000}
print(dict_check_small_values(d, 7000))