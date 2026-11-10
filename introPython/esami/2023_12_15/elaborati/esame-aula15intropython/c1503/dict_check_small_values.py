def dict_check_small_values(d,threshold) :
    for k in d :
        if d[k]>=threshold :
            return False
    return True
a = {"gsa" : 12 , "gf" : 65 , "ghedw" : 9}
b = dict_check_small_values(a,66)
print(b)