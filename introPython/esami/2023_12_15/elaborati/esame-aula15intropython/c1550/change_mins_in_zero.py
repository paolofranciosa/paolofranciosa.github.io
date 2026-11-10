'''Write a function change_mins_in_zero(values) that:
• expects a non-empty list of comparable values as an argument;
• directly modifies the values list by replacing the minimum values with
zero.
If the minimum appears several times in the list, the function must replace
all occurrences of the minimum value with zero.'''

def change_mins_in_zero(values):
    minimo=values[0]
    for e in values:
        if e<minimo:
            minimo=e
    for i in range(len(values)):
        if values[i]==minimo:
            values[i]=0
    return values