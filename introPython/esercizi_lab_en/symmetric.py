def symmetric(M):
    for r in range(0, len(M)):
        for c in range(0, len(M[0])):
            if M[r][c] != M[c][r]:
                return False
    return True    
