def separaelementi(valori):

    if len(valori) == 0:
        raise ValueError

    for x in valori:
        if not isinstance(x, (int, float)):
            raise TypeError

    media = sum(valori) / len(valori)

    left = [x for x in valori if x > media]
    right = [x for x in valori if x <= media]

    return left, right

