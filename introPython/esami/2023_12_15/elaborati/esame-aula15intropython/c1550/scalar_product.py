'''Write a function scalar_product that:
• takes two non-empty lists a, b with the same length as parameters,
where each element is a number (int or float);
• returns the scalar product of the two lists'''

def scalar_product(a,b):
    prodotto=0
    for i in range(len(a)):
        prodotto += a[i]*b[i]
    return prodotto