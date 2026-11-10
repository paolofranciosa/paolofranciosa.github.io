def dict_check_small_values(d, treshold):
    contatore = 0
    for key in d:
        if d[key] < treshold:
            contatore = contatore + 1
    if (contatore == len(d)): 
        return True
    else:
        return False
     

d = {"Mario": 1000, "Gianna":8000, "Alberto":4000}
print(d["Mario"])
    
    
print(dict_check_small_values(d, 9888))

    