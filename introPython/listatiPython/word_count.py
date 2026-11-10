def word_count(text):

    if not isinstance(text, str):
        raise TypeError

    counter = 0
    if len(text) == 0:
        return 0
    for i in range(len(text) - 1):
        this_char = text[i]
        next_char = text[i+1]
        if (this_char.isalpha() or this_char.isdigit()) and not ((next_char.isalpha() or next_char.isdigit())):
            counter += 1

    last_char = text[len(text) - 1]
    if (last_char.isalpha() or last_char.isdigit()):
        counter += 1
    return counter

print(word_count("hi, I am Jack3"))