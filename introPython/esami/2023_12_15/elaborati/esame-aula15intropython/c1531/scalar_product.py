def scalar_product(a, b): # in input 2 liste
    prodInterno=1
    prodS=0
    for i in range(len(a)): 
            prodInterno = a[i]*b[i]
            prodS = prodS + prodInterno
    return prodS
            
    
    
    
    
    
    
# in output voglio il prodotto scalare  
    
l1 = [1,4,3]
l2 = [5,5,1]

print(scalar_product(l1, l2))