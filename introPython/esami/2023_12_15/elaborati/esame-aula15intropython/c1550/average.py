'''Write a function average(L) that,
• takes a list L as parameter, in which each element is a number (int or
float);
• returns the average of all numbers in the list L. You can assume that L
is a list of numbers (each element is int oppure float).'''

def average(L):
    l=len(L)
    somma=0
    for e in L:
        somma+=e
    media=somma/l
    return media

