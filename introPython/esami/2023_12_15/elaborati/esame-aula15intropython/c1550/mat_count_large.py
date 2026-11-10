'''Write a function mat_count_large(m, threshold) that:
• takes as argument a matrix m, represented as a list of lists;
• returns the number of elements in m that are strictly larger than
threshold.
We represent an r × c matrix in Python as a list with length r, where
each element is a list of length c. You may assume that the argument is
well formed, with r ≥ 1, c ≥ 1, and all the lists representing rows contain
c numeric elements.'''

def mat_count_large(m, threshold):
    c=0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>threshold:
                c+=1
    return c