def almost_equal(a, b):

    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError
    if len(a) != len(b):
        raise ValueError
    for i in range(len(a)):
        if not isinstance(a[i], (int, float)) or not isinstance(b[i], (int, float)):
            raise TypeError

    for i in range(len(a)):
        if abs(a[i]-b[i]) > 1:
            return False
    return True

