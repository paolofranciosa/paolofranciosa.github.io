'''range(START VALUE, END VALUE, STEP)   "sequence from START (included) to END (not included) by STEP"
range(10)   ->  0, 1, 2, 3, 4, ..., 9
range(5, 8)  ->  5, 6, 7
range(2, 10, 3)  ->  2, 5, 8
'''

# scan a sequence by positions
def vowel_count(phrase):
    '''phrase is a sequence of characters, returns the number of vowels'''
    counter = 0
    for x in phrase:  # x is iterating on elements of a sequence
        if x in "aeiou":  # True if x occurs in the sequence
            counter += 1
    return counter
    
# count the vowels in a phrase
# scan the sequence, incrementing a counter any time i find a vowel

s = "asdgutasdhgasfdtyfa"
s1 = "aaaabdeeeb  ee"
print("there are", vowel_count(s), "vowels in", '"'+s+'"')
print("there are", vowel_count(s1), "vowels in", '"'+s1+'"')
