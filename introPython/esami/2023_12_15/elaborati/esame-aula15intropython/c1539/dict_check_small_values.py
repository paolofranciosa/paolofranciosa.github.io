def dict_check_small_values(d,threshold):
    for i in d:
        if d[i]>=threshold:
            return False
    return True
d1={'mario':1000,'luca':8000,'marco':6000}
s=dict_check_small_values(d1,7000)
print(s)
d2={'mario':1000,'luca':8000,'marco':6000}
s=dict_check_small_values(d1,9000)
print(s)
    
    