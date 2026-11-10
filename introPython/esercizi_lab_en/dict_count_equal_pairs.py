def dict_count_equal_pairs(d):
    count = 0
    for k in d:
        if d[k] == k:
            count += 1
    return count

