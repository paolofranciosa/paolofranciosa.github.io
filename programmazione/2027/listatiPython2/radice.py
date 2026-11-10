def radice(x, eps=1e-13):
    sol = x/2
    while abs((sol - x/sol)/sol) > eps:
        sol = (sol+x/sol)/2
    return sol

if __name__ == "__main__":
    print(radice(2))
    print(radice(101))
    print(radice(2345678))
    print(radice(2**30*10**30))
    print(radice(0.25))
    