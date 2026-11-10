def dict_check_small_values(d, threshold):
    v=True
    for k in d:
        if d[k]>=threshold:
            v=False
    return v


d= {"Mario": 1000, "Gianna" : 8000, "Alberto": 4000}
print(dict_check_small_values(d, 500))
print(dict_check_small_values(d, 2000))
print(dict_check_small_values(d, 8000))
print(dict_check_small_values(d, 8001)) 