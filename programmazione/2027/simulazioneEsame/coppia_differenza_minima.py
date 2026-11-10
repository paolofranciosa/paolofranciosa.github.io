def coppia_differenza_minima(L):

    S = sorted(zip(L, range(len(L))))
    mindist = abs(S[0][0] - S[1][0])
    pos = [S[0][1], S[1][1]]

    for i in range(2, len(L)):
        d = abs(S[i - 1][0] - S[i][0])
        if d < mindist:
            mindist = d
            pos = (S[i - 1][1], S[i][1])

    return sorted(pos)

