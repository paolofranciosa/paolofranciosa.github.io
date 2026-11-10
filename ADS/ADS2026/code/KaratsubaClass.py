# da completare includendo il trattamento dei segni per ora è tutto positivo)
# e implementando i metodi __mul__ ed __rmul__

class BigInteger:
    '''represents a natural number as a reversed list of digits, where each
digit is a character.
Implements sum, subtraction and multiplication (not yet). All operations are assumed
to have positive operands and positive result.
Multiplication is implemented by Karatsuba algorithm'''
    def __init__(self, val):
        '''builds a new BigInteger containing a value'''
        self.__positive = val >= 0
        if not self.__positive:
            val = - val
        self.__digits = [int(c) for c in str(val)[::-1]]  # private variable storing information
#        print(self.__digits)
    
    def __str__(self):
        return str(self.get_value())
        
    def get_value(self):
        '''returns the int value, with sign'''
        result = int("".join([str(c) for c in self.__digits[::-1]]))
        if not self.__positive:
            result = "-" + result
        return result


    def is_zero(self):
        '''returns True if and only if the number is zero'''
        return len(self.__digits) == 1 and self.__digits[0] == 0
    
    def __eq__(self, value):
        return self.get_value() == value.get_value()
    
    def __ne__(self, value):
        return not self.__eq__(value)
    
    def __gt__(self, value):
        return self.get_value() > value.get_value()
        
    def __ge__(self, value):
        return self.get_value() >= value.get_value()
        
    def __lt__(self, value):
        return self.get_value() < value.get_value()
        
    def __le__(self, value):
        return self.get_value() <= value.get_value()

    def __add__(self, value):
        '''returns the sum of self and value'''
        if isinstance(value, int):
            value = BigInteger(value)
        a = self.__digits
        b = value.__digits
        result = BigInteger(0)

        if self.__positive == value.__positive: # same sign
            result.__digits = BigInteger.add_digits(a, b)
            result.__positive = self.__positive
        elif self.__positive:
            if 
            

        return result

    def __radd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        '''returns the difference self - value, assuming it is not negative'''
        if isinstance(value, int):
            value = BigInteger(value)
        a = self.__digits
        b = value.__digits
        result = BigInteger(0)
        result.__digits = BigInteger.sub_digits(a, b)
        return result

    def __rsub__(self, value):
        if isinstance(value, int):
            value = BigInteger(value)
        return value.__sub__(self)

    def add_digits(a, b):
        '''class method. Returns the list representing a+b,
where a and b are lists representing positive integers'''
        c = []
        remainder = 0
        min_len = min(len(a), len(b))
        for i in range(min_len):
            digits_sum = a[i] + b[i] + remainder
            c.append(digits_sum % 10)
            remainder = digits_sum // 10
        if len(a) > len(b):
            for i in range(min_len, len(a)):
                digits_sum = a[i] + remainder
                c.append(digits_sum % 10)
                remainder = digits_sum // 10
        else:
            for i in range(min_len, len(b)):
                digits_sum = b[i] + remainder
                c.append(digits_sum % 10)
                remainder = digits_sum // 10
        if remainder == 1:
            c.append(1)
        return c
    
    def sub_digits(a, b):
        '''class method. Returns the list representing a-b,
where a and b are lists representing positive integers
and a-b is assumed to be not negative'''
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
        '''class method. Returns the n, n+1, ... most significant digits of digit list a.
    Returns [0] if there are no such digits'''
        if len(a) <= n:
            return [0]
        return a[n:]

    def add_zeroes(a, n):
        '''class method. Returns the digit list a with n least significant zeroes attached'''
        return [0]*n + a

    def low_part(a, n):
        '''class method. Returns the n least significant digits of digit_list a'''
        return a[:n]

    def mult_digit(a, b):
        '''class method. a and b are digit lists of length 1.
    Returns the list representing the sum, in reversed order, so that
    [7] + [5] = [2, 1]
    The result lenght is either 1 or 2'''
        res = a[0] * b[0]
        if res < 10:
            return [res]
        else:
            return [res % 10, res // 10]
        
    def multiply(a, b):
        '''class method. Returns the digit list of a*b, applying Karatsuba algorithm'''
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
    a = BigInteger(2567)
    b = BigInteger(255243786348)
    c = BigInteger(70)
    print(a > b)
    print(a > c)
    print(b + 34)
    print(a-c)
    print(a-10)
    print(3000-a)
