import networkx as nx
import time

def inputGraphFromFile(nome_file_colori, nome_file_rete, grafo, colors, colorGroups, soglia_peso=700, isolated=False):
    '''legge un grafo da files.
        nome_file_colori è un file che contiene per ciascuna riga il nome di un nodo e il relativo colore
                         il colore può essere assente, in tal caso si intende valga "X"
        nome_file_rete   è un file che contiene coppie di archi. Può contenere o meno archi simmetrici
                         (il grafo si intende comunque non orientato).
                         Può contenere archi i cui estremi non figurano nel file nome_file_colori:
                         in tal caso vengono inseriti anche i nodi, con colore "X".
                         Può essere presente un peso per ciascun arco: in tal caso si inserirà 
                         l'arco solo se il peso è maggiore o uguale alla soglia_peso
        soglia_peso      regola l'inserimento degli archi. Se non specificata si intende 700
                         gli archi inseriti avranno comunque peso 1
        grafo            è inizialmente un grafo (networkx) vuoto
        colors           è il set di colori presenti nel grafo (inizialmente vuoto)
        colorGroups      è il set di colorGroups presenti nel grafo (inizialmente vuoto)
        isolated         se True inserisce nel grafo anche i nodi isolati
        
    '''
    aggiungiArchi(grafo, nome_file_rete, soglia_peso)
    leggiColori(grafo, nome_file_colori, isolated)
    popolaColori(grafo, colors, colorGroups)
    
def prefisso(s):
    if "_" in s:
        return s[:s.index("_")]
    else:
        return s 

def leggiColori(grafo, nomefile, isolated):
    '''Legge da file un elenco di nodi con i colori.
Aggiunge ai nodi un attributo pari al colore letto e al gruppo di colori
Nel file dei nodi possono comparire nomi con estensione "xxx_y".
Nella lettura degli archi le estensioni vengono eliminate.
Quando si scandisce un nodo con estensione si verifica se il nodo è già presente con un colore:
- se il colore è vuoto oppure coincide con il colore scandito
     si assegna il colore scandito
- altrimenti (è presente un colore diverso da quello scandito)
     si assegna il colore "X"'''
    f_in = open(nomefile)
    for riga in f_in:
        campi = riga.split()
        nodo = prefisso(campi[0]).upper()
        if len(campi) == 1:
            colore = "X"
            colGroup = "X"
        else:
            colore = campi[1]
            if colore in "RS":
                colore = "X"
            if colore in "JAKLB":
                colGroup = "JAKLB"
            elif colore in "DYVTMNZWUO":
                colGroup = "DYVTMNZWUO"
            elif colore in "CGEFHIPQ":
                colGroup = "CGEFHIPQ"
            elif colore in "RSX":
                colGroup = "X"  
            else:
                colGroup = campi[1]
        if nodo not in grafo.nodes() and isolated:  # se è un nodo isolato deve essere aggiunto
                                                   # solo se esplicitamente richiesto
            grafo.add_node(nodo, color = "", colorGroup = "colGroup")
        if nodo in grafo.nodes():
            oldColor = grafo.nodes[nodo]['color']
            if oldColor != "" and oldColor != colore:
                colore = "X"
                colGroup = "X"  
            grafo.add_node(nodo, color = colore)
            grafo.add_node(nodo, colorGroup = colGroup)
    for nodo in grafo.nodes:
        if grafo.nodes[nodo]['color'] == "":
            grafo.add_node(nodo, color="X", colorGroup="X")

# l'aggiunta del colore e del gruppo di colori ai due set (colors e colorGroups)
# viene eseguita dalla funzione popolaColori

def popolaColori(grafo, colors, colorGroups):
    '''scorre l'elenco dei nodi, aggiungendo colore e gruppo di colori ai set
       colors e colorGroups.'''
    for nodo in grafo.nodes:
        colors.add(grafo.nodes[nodo]['color'])
        colorGroups.add(grafo.nodes[nodo]['colorGroup'])
    
def aggiungiArchi(grafo, nomefile, soglia_peso):
    '''Legge da file una sequenza di archi rete e li aggiunge al grafo in formato networkx,
       aggiungendo ai nodi i nodi estremi dell'arco. L'arco viene aggiunto in entrambe le
       liste di adiacenza (se non già presente)
Si assume che nel file di input possa essere presente una coppia simmetrica di archi per ciascuna coppia di nodi adiacenti.
'''
    f_in = open(nomefile)
    for riga in f_in:
        campi = riga.split()
        nodo1 = prefisso(campi[0]).upper()
        nodo2 = prefisso(campi[1]).upper()
        if len(campi) == 3:
            peso = int(campi[2])
            if peso >= soglia_peso:
                grafo.add_node(nodo1, color="", colorGroup="")
                grafo.add_node(nodo2, color="", colorGroup="")
                grafo.add_edge(nodo1, nodo2)
                grafo.add_edge(nodo2, nodo1)
#                grafo.add_edge(campi[0], campi[1], weight = peso)
#                grafo.add_edge(campi[1], campi[0], weight = peso)
        else:
            grafo.add_node(nodo1, color="", colorGroup="")
            grafo.add_node(nodo2, color="", colorGroup="")
            grafo.add_edge(nodo1, nodo2)
            grafo.add_edge(nodo2, nodo1)
#            grafo.add_edge(campi[0], campi[1], weight = soglia_peso)
#            grafo.add_edge(campi[1], campi[0], weight = soglia_peso)

def scriviGrafo(grafo, nome_file_rete_out, nome_file_colori_out):
    f_rete = open(nome_file_rete_out, "w")
    f_colori = open(nome_file_colori_out, "w")
    for arco in grafo.edges():
        print(arco[0], arco[1], file = f_rete)
    f_rete.close()
    for nodo, colore in grafo.nodes.data('color'):
        print(nodo, colore, file = f_colori)
    f_colori.close()