def conteggiovocali(testo):

    vocali = 'AEIOUaeiouàèìòùÀÈÌÒÙÉé'

    counter = 0
    for c in testo:
        if c in vocali:
            counter += 1
    return counter

