def word_count(testo):

    if not isinstance(testo, str):
        raise TypeError

    counter = 0
    inword = False
    for c in testo:
        wordchar = c.isalpha() or c.isdigit()
        if wordchar:
            if not inword:
                counter += 1
            inword = True
        else:
            inword = False

    return counter

