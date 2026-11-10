import time
import random

def concatenate_strings_1(many_words):
    '''given a list of strings, returns its concatenation
A trivial implementation requires time proportional to the sum of the cumulative sum
of string length that is quadratic in the number of strings'''
    res = ""
    for w in many_words:
        res += w
    return res

def concatenate_strings_2(many_words):
    '''given a list of strings, returns its concatenation
A trivial implementation requires time proportional to the sum of the cumulative sum
of string length that is quadratic in the number of strings'''
    res = ""
    for w in many_words:
        new = res + w
        res = new
    return res

def concatenate_smart(many_words, start = None, end = None):
    if end is None:
        return concatenate_smart(many_words, 0, len(many_words) - 1)
    if end == start:
        return many_words[start]
    else:
        mid = (start + end) // 2
        a = concatenate_smart(many_words, start, mid)
        b = concatenate_smart(many_words, mid + 1, end)
        return a + b
    
def build_word_list(word, dim):
    minimum = 10**20
    maximum = 10**21-1
    return [str(random.randint(minimum, maximum)) for i in range(dim)]

min_exp = 15
max_exp = 19
print('concatenate_smart\n' + f'{"num":^10s} {"time":^10s}')
for num in [2**i for i in range(min_exp, max_exp)]:
    start = time.time()
    l = build_word_list("pippo", num)
    conc = concatenate_smart(l)
    dur = time.time() - start
    print(f'{num:10d} {dur:10.3f}')

print('concatenate_trivial_1\n' + f'{"num":^10s} {"time":^10s}')
for num in [2**i for i in range(min_exp, max_exp)]:
    start = time.time()
    l = build_word_list("pippo", num)
    conc = concatenate_strings_1(l)
    dur = time.time() - start
    print(f'{num:10d} {dur:10.3f}')
    
print('concatenate_trivial_2\n' + f'{"num":^10s} {"time":^10s}')
for num in [2**i for i in range(min_exp, max_exp)]:
    start = time.time()
    l = build_word_list("pippo", num)
    conc = concatenate_strings_2(l)
    dur = time.time() - start
    print(f'{num:10d} {dur:10.3f}')
    
    