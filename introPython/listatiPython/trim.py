def trim(s, trim_chars=" "):
    res = ""
    
    i = 0
    while i < len(s) and s[i] in trim_chars:
        i += 1
    inizio = i
    
    if i == len(s):
        return ""

    i = len(s) -1
    while i >= 0 and (s[i] in trim_chars):
        i -= 1
    fine = i
    
    return s[inizio : fine+1]

prova = input("scrivi una stringa, anche con spazi in testa e/o in coda")
print("stringa originaria: '" + prova +"'")
print("trim: '" + trim(prova)+"'")