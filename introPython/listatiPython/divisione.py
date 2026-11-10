def divisione(a,b):
    if b == 0:
        raise ValueError("non posso dividere per zero")
    return a/b

if __name__ == "__main__":
    print(divisione(34, 5))
    print(divisione(34, 0))
    