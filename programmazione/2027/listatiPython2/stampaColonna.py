def stampa_verticale(s1, s2):
    if len(s1) < len(s2):
        l_min = len(s1)
    else:
        l_min = len(s2)
    
    for i in range(l_min):
        print(s1[i]+"  "+s2[i])
    
    if len(s1) > len(s2):
        for i in range(l_min, len(s1)):
            print(s1[i])
    else:
        for i in range(l_min, len(s2)):
            print("   "+s2[i])
            
stampa_verticale("Ciao", "Anna")
print()
stampa_verticale("Ciao", "Giovanni")
print()
stampa_verticale("Ciao", "Pa")
