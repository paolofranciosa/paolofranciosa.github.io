def scalar_product(a,b):
    prod = 0
    for i in range(len(a)):
        num=a[i]*b[i]
        prod=prod+num
    return prod