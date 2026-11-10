def scalar_product(a,b):
    r = 0
    for i in range(len(a)):
        s = a[i]*b[i]
        r += s
    return r

H = [1, 4, 3]
O = [5, 5, 1]
print(scalar_product(H,O))