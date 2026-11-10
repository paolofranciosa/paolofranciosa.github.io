def to_list(n):
    '''returns the representation of natural n by the reverse list of digits as characters'''
    return [int(c) for c in str(n)[::-1]]
    
def to_num(list_n):
    '''starting from by the reverse list of digits as characters, returns the int value'''
    return int("".join([str(c) for c in list_n[::-1]]))

def sum_numbers(a, b):
    '''returns the sum of two natural numbers'''
    c = []
    remainder = 0
    for i in range(min(len(a), len(b))):
        digits_sum = a[i] + b[i] + remainder
        c.append(digits_sum % 10)
        remainder = digits_sum // 10
    if len(a) > len(b):
        for i in range(min(len(a), len(b)), len(a)):
            digits_sum = a[i] + remainder
            c.append(digits_sum % 10)
            remainder = digits_sum // 10
    else:
        for i in range(min(len(a), len(b)), len(b)):
            digits_sum = b[i] + remainder
            c.append(digits_sum % 10)
            remainder = digits_sum // 10
    if remainder == 1:
        c.append(1)
    return c

def diff_numbers(a, b):
    '''returns the difference a-b, assuming it is not negative'''
    c = []
    remainder = 0
    for i in range(min(len(a), len(b))):
        digit_sum = a[i] - b[i] - remainder
        if digit_sum >= 0:
            c.append(digit_sum)
            remainder = 0
        else:
            c.append(digit_sum + 10)
            remainder = 1
    if len(a) > len(b):
        for i in range(min(len(a), len(b)), len(a)):
            digit_sum = a[i] - remainder
            if digit_sum >= 0:
                c.append(digit_sum)
                remainder = 0
            else:
                c.append(digit_sum + 10)
                remainder = 1
    else:
        for i in range(min(len(a), len(b)), len(b)):
            digit_sum = b[i] - remainder
            if digit_sum >= 0:
                c.append(digit_sum)
                remainder = 0
            else:
                c.append(digit_sum + 10)
                remainder = 1
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c

def high_part(a, n):
    '''returns the n, n+1, ... most significant digits of a.
Returns [0] if there are no such digits'''
    if len(a) <= n:
        return [0]
    return a[n:]

def add_zeroes(a, n):
    '''returns a with n least significant zeroes attached'''
    return [0]*n + a

def low_part(a, n):
    '''returns the n least significant digits of a'''
    return a[:n]

def mult_digit(a, b):
    '''a and b are list of digits of length 1.
Returns the list representing the sum, in reversed order, so that
[7] + [5] = [2, 1]
The result lenght is either 1 or 2'''
    res = a[0] * b[0]
    if res < 10:
        return [res]
    else:
        return [res % 10, res // 10]
    
def multiply(a, b):
    if len(a) == 1 and len(b) == 1:
        return mult_digit(a, b)
    else:
        n = max(len(a), len(b)) // 2
        a0 = low_part(a, n)
        b0 = low_part(b, n)
        a1 = high_part(a, n)
        b1 = high_part(b, n)
        
        A = multiply(a0, b0)
        B = multiply(sum_numbers(a0, a1), sum_numbers(b0, b1))
        C = multiply(a1, b1)
        mid_term = diff_numbers(B, sum_numbers(A, C))

        result = sum_numbers(sum_numbers(add_zeroes(C, 2*n), add_zeroes(mid_term, n)), A)
        return result
    
if __name__ == "__main__":
    x_n = 32457893487684356536403246845
    y_n = 4555345654345635465465456456456456456234
    x = to_list(x_n)
    y = to_list(y_n)
    res = to_num(multiply(x,y))
    print(f'{x_n} * {y_n} = {res}')
    print(x_n*y_n == res)
    
    