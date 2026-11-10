'''           |  1              if  n = 0 or n = 1
   fact(n) =  |
              |  n * fact(n-1)  if  n > 1
'''

def fact(n):
    if n < 0:
        raise ValueError
    if n <= 1:
        return 1
    return n * fact(n-1)

print(10,fact(10))
print(10.5,fact(10.5))
print(-5,fact(-5))
print("www",fact("www"))
