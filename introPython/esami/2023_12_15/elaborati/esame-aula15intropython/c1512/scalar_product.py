def scalar_product(a, b):
    if isinstance (a, list):
        if isinstance (b, list):
            if len(a) == len(b):
                summ = 0
                for i in range(len(a)):
                    summ = summ + a[i]*b[i]
                return summ
            else:
                print("The lengths of a and b are not equal.")
        else:
            print("b is not a list.")
    else:
        print("a is not a list.")
        
        