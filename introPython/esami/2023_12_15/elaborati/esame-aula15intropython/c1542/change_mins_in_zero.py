import math
def change_mins_in_zero(values):
    minimum = min(values)
    for i in range(len(values)):
        if values[i] == minimum:
            values[i] = 0
        
        
    return values
print(change_mins_in_zero((2, 3, 4)))