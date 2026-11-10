def scalar_product(a,b):
    result=0
    for i in range(len(a)):
        result+=a[i]*b[i]
    return result

a=[1,4,3]
b=[5,5,1]
print(scalar_product(a,b))