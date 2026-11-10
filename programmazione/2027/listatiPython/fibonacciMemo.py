fibs = {0:0, 1:1} # variabile globale: accessibile da qualunque funzione in questo file

def fibonacci(n):
    global fibs  # questa funzione può modificare fibs
    if n in fibs: # 
        return fibs[n]
    else:
        fibs[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibs[n]

if __name__ == "__main__": # chiamata di prova
    print(fibonacci(50))
    