import math

def prime(n):
    if n < 2:
        return False
    for div in range(2,n):
        if n % div == 0:
            return False
        div = div+1
    return True

def fast_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(math.sqrt(n))
    for div in range(3, max_div + 2, 2):
        if n % div == 0:
            return False
        div = div+1
    return True

if __name__ == "__main__":
    while True:
        num = int(input("write a number (0 to finihs): "))
        if num != 0:
            if fast_prime(num):
                print(str(num) + " is prime")
            else:
                print(str(num) + " is composite, ", end="")
                for n in range(num, num//2, -1):
                    if fast_prime(n):
                        print("but {} is prime".format(n))
                        break
        else:
            break
    print("bye")