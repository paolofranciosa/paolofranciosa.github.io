def dict_check_small_values(d,threshold):
    for i in d.values():
        if i >= threshold:
            return False
    return True

print(dict_check_small_values({"Gianna" : 8000,"Mario":1000, "Alberto":4000},8000))