def cumulated_list(valori):
    res = [valori[0]]
    for i in range(1, len(valori)):
        res.append(res[i-1] + valori[i])
    return res
