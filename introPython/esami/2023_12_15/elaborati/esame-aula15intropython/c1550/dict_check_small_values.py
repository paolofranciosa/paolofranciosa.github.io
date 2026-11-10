'''Write a function dict_check_small_values(d, threshold) that:
• takes as arguments a dictionary d with values of type int or float and
an number threshold;
• returns True if all values are strictly smaller than threshold, and
returns False otherwise.
You may assume that alle values are numeric.'''

def dict_check_small_values(d, threshold):
    for k in d:
        if d[k] >= threshold:
            return False
    return True