def poly_product(a,b):
    prod_degree = (len(a)-1) + (len(b)-1)
    prod = [0] * (prod_degree + 1)
    for a_deg in range(len(a)):
        for b_deg in range(len(b)):
            term_degree = a_deg + b_deg
            prod[term_degree] += a[a_deg]*b[b_deg]
    return prod

def print_poly(p):
    row = ""
    for deg in range(len(p)-1, -1, -1):
        if p[deg] != 0:
            row += str(p[deg])
            if deg != 0:
                row += "x"
                if deg > 1:
                    row += "^"+str(deg)
                row += "+"
    return row

print(poly_product([2,3,1],[4,5,3,0]))
print(poly_product([1,1,1,1,1,1,1],[-1,1]))

x,y = [2,3,1],[4,5,3,0]
print(print_poly(x), "*", print_poly(y), "=", print_poly(poly_product(x,y)))
x,y = [1,1,1,1,1,1,1],[-1,1]
print(print_poly(x), "*", print_poly(y), "=", print_poly(poly_product(x,y)))

