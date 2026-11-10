def f(i):
    a = 1
    while i >= 1:
        a *= i
        i -= 1
    return a

for i in range(11):
    print(f(i))
    