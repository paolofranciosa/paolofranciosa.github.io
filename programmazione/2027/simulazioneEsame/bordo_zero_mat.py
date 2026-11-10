def bordo_zero_mat(M):
    r = len(M)
    c = len(M[0])

    # top
    for j in range(c):
        if M[0][j] != 0:
            return False

    #left
    for i in range(r):
        if M[i][0] != 0:
            return False

    #right
    for i in range(r):
        if M[i][-1] != 0:
            return False

    #bottom
    for i in range(c):
        if M[-1][i] != 0:
            return False
    return True

