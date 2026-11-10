def num_over_threshold(d, t):
    '''given a dict, return the number of values larger that t'''
    count = 0
    for k in d:
        # check whether that value is large
        if d[k] > t: 
            count += 1
    return count
    
def keys_over_threshold(d, t):
    '''return a list of keys containing all the keys with
values larger than t'''
    res = []
    for k in d:
        if d[k] > t:
            res.append(k)
    return res
    
    
d = {"a":20, "b":30, "c":25, "d": 10, "e": 15}
print(num_over_threshold(d, 15))  # 3
print(keys_over_threshold(d, 20)) # ["a", "b", "c"]