def sommaInteriDaFile(nomeFile) :
    somma = 0
    with open(nomeFile) as inputFile :
        for r in inputFile :
            for num in r.split() :
                somma += float(num)
    return somma

def sommaInteriDaFileBis(nomeFile) :
    somma = 0
    inputFile = open(nomeFile)
    for r in inputFile :
        for num in r.split() :
            somma += float(num)
    return somma

nomeFile = input("scrivi nome del file: ")
print("la somma è", sommaInteriDaFileBis(nomeFile))