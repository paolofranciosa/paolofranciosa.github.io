def quad_ast(n):
    '''stampa un quadrato n x n di asterischi'''
    for i in range(n):
        for j in range(n):
            print("*", end="") # il parametro end="" fa in modo che non vada a capo ad ogni print
        print() # questo serve ad andare a capo
        
quad_ast(10)
quad_ast(4)