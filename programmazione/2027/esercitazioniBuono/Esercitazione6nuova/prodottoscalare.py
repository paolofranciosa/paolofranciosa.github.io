def prodottoscalare(a, b):

    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError
    if len(a) != len(b):
        raise ValueError
    for i in range(len(a)):
        if not isinstance(a[i], (int, float)) or not isinstance(b[i], (int, float)):
            raise TypeError

    acc = 0
    for i in range(len(a)):
        acc += a[i] * b[i]

    return acc

