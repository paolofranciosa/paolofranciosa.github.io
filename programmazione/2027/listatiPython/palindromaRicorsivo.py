def palindroma(frase):
    '''metodo ricorsivo per verificare se una sequenza è palindroma'''
    if len(frase) < 2:
        return True
    if frase[0] != frase[-1]:
        return False
    return palindroma(frase[1:-1])
    
if __name__ == "__main__":
    print("abccba", palindroma("abccba"))
    print("abcba", palindroma("abcba"))
    print("asdfsdb",palindroma("asdfsdb"))
    print("adfghsfa",palindroma("adfghsfa"))
    print("abcdfghdfhgcba",palindroma("abcdfghdfhgcba"))
    print("aa",palindroma("aa"))