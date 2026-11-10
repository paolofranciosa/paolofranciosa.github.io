def scalar_product(a,b):
    scalar_prod=0
    if len(a)!=0 and len(a)==len(b):
        for i in range(0,len(a)):
            scalar_prod+=a[i]*b[i]
        return (scalar_prod)
    else:
        print ("The two lists must have the same length and not empty")
print(scalar_product([],[]))