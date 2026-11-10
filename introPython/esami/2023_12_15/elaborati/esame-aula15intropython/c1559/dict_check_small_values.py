def dict_check_small_values(d, threshold):
    count = 0
    for i in d:
        if d[i] > threshold:
           count = count + 1
    if count == len(d):
       print(True)
    else:
        print(False)
    return    
       
    
d = {"a":10000,"b":7000,"c":5000}
limite = 400
print(dict_check_small_values(d,limite))