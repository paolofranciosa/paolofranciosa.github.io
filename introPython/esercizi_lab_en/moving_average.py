def moving_average(seq, k):
    if not isinstance(seq, list):
        raise TypeError
    for x in seq:
        if not isinstance(x, (int, float)):
            raise TypeError

    if len(seq) < k or k < 1:
        raise ValueError

    medie = [0]
    for i in range(k):
        medie[0] += seq[i]

    for i in range(k, len(seq)):
        medie.append(medie[-1] + seq[i] - seq[i - k])
    for i in range(len(medie)):
        medie[i] /= k

    return medie

