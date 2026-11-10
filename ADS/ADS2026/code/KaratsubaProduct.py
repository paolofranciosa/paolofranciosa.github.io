'''compute the product of two natural numbers by Karatsuba algorithm.
a * b, where   a is the concatenation of a1, a2   a = a1*10^k + a2
               b is the concatenation of b1, b2   b = b2*10^k + b2
a*b = a1*b1*10^(2k) + (a1*b2 + a2*b1)*10^k + a2*b2
In order to obtain the theoretically expected complexity, operations **10^k and // 10^k
should be substituted by low-level shift operations in base 2.
This code is for demonstration only.'''

def length(x):
    '''given a natural number x, returns the number of digits in the decimal representation of x'''
    return len(str(x))

def mult(a, b):
    if length(a) == 1 and length(b) == 1:
        return a*b
    split_pos = max(length(a), length(b)) // 2  #  split_pos is what we called k above
    a1 = a // 10**split_pos
    a2 = a % 10**split_pos
    b1 = b // 10**split_pos
    b2 = b % 10**split_pos
    A = mult(a1, b1)
    B = mult(a2, b2)
    C = mult(a1+a2, b1+b2)
    return A*10**(2*split_pos) + (C-A-B)*10**split_pos + B


x = int(input("scrivi un numero: "))
y = int(input("scrivi un numero: "))

print("{} * {} = {}, (correct value is {})".format(x, y, mult(x, y), x*y))