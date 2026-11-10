def scalar_product(a,b):
    total = 0
    for i in range(len(a)):
        total = total + (a[i]*b[i])
    return total
