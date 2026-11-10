def add_union(a, b):
    for x in b:
        if x not in a:
            a.append(x)
