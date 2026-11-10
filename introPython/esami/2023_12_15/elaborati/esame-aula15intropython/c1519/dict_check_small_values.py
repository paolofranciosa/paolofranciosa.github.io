def dict_check_small_values(d, treshold):
    conta=0
    for i in d.keys():
        if d[i]>=treshold:
            break
        else:
            conta+=1
    if conta==len(d):
        return (True)
    else:
        return (False)
print(dict_check_small_values({"Mario": 1000, "Gianna" : 8000, "Alberto": 4000},9000))