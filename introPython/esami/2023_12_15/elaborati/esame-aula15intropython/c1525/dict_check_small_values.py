def dict_check_small_values(d, t):
    if not isinstance(d,dict):
        raise TypeError
    for i in d:
        if not isinstance(d[i],int) and not isinstance(d[i],float):
            raise TypeError
    
    if not isinstance(t,int) and not isinstance(t,float):
        raise TypeError
    for i in d:
        if d[i] >= t:
            return False
    return True
d = {"Mario": 1000, "Gianna" : 8000, "Alberto": 4000}
print(dict_check_small_values(d, 7000))