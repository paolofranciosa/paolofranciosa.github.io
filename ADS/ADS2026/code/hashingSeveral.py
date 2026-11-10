'''implements hash table with linear probing using fixed step'''

dimension = 19
step = 1
hash_tab = [""] * dimension

def simple_hash(word):
    '''returns an integer in [0,n) starting from a string'''
    tot = 0
    for c in word:
        tot += ord(c)**3
    return (tot // 100) % dimension

def second_simple_hash(word):
    '''returns an integer in [0,n) starting from a string'''
    tot = 0
    for c in word:
        tot += ord(c)**5
    return (tot // 100) % dimension

# THIS IS LINEAR
def insert_linear(word):
    position = simple_hash(word)
    num_probes = 1
    while hash_tab[position] != "":
        position = (position + step) % dimension
        num_probes += 1
    hash_tab[position] = word
    return num_probes

# THIS IS QUADRATIC
def insert_quadratic(word):
    start = simple_hash(word)
    num_probes = 1
    position = start
    while hash_tab[position] != "":
        position = (start + num_probes**2) % dimension
        num_probes += 1
    hash_tab[position] = word
    return num_probes

# THIS IS double hashing
def insert_double(word):
    position = simple_hash(word)
    my_step = second_simple_hash(word)
    num_probes = 1
    while hash_tab[position] != "":
        position = (position + my_step) % dimension
        num_probes += 1
    hash_tab[position] = word
    return num_probes

def show_insert(word):
    print(word, insert_quadratic(word))
    
show_insert("Paolo")
show_insert("Giulio")
show_insert("Franciosa")
show_insert("a")
show_insert("b")
show_insert("c")
show_insert("d")
show_insert("e")
show_insert("f")
show_insert("g")
show_insert("h")
show_insert("i")
show_insert("l")
print("\n\nHASH TABLE")
print("\n".join(hash_tab))
