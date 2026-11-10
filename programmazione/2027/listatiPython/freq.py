def frequency(sequence):
    '''sequence is a list of element,
e.g., [11, 22, 66, 11, 55, 66, 22, 22, 88].
Return a dict, in which each distinct element of seq is
associate to the number of occurrences in sequence
{11: 2, 22: 33, 66: 2, 55: 1, 88: 1}'''
    counters = dict()
    # for each element in sequence we increase the corresponding value
    for elem in sequence: # elem is already a key of counters
        if elem in counters: # already exists 
            counters[elem] = counters[elem] + 1
        else: # add a new item in the dict
            counters[elem] = 1
    return counters

def word_freq(t):
    # get the list of words from t
    # compute frequences from that list
    # return the result
    word_seq = text.split()
    f = frequency(word_seq)
    return f
        
text = "My cat is playing with my dog on my chair"
res = word_freq(text)
print(res)

            
        