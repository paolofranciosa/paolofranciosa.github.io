#############################################################################
#
# A software prototype for measuring the homophily/heterophily of a network as described in paper
# A novel method for assessing and measuring homophily in networks
# by Nicola Apollonio, Paolo G. Franciosa, Daniele Santoni
# 
##############################################################################
# Software author: Paolo Giulio Franciosa  paolo.franciosa@uniroma1.it
#                  Dept of Statistics
#                  Sapienza University of Rome, Italy
##############################################################################
# 
# The input network must be described by two text files:
# 
# - an edge file, where each line defines an edge in the format
#   UUU VVV WEIGHT
#   where UUU and VVV are two strings (no quotes) representing the nodes,
#   and WEIGHT is an integer number in 0-999 representing the score.
#   Field WEIGHT may be omitted, in this case the edge is NOT discarded
#   Pairs of symmetric edges are allowed, and only one is considered in the resulting undirected graph.
# 
# - a node file, where each line defines a node and its color, in the format
#   UUU C
#   where UUU is the node label (as in the edge file) and C is a character defining node's color
# 
# The program is launched by command
# python3 graphColorStatisticsPublic.py edgeFile nodeFile weight_threshold
# where threshold can be omitted (default = 700)
# 
# The program writes an eps file containing a heatmap of edge zscores,
# and two files containing values of edges zscores and singleton zscores.
# Computing times are given on standard output.
# 
##############################################################################


import networkx as nx
import math
import readGraph
import time
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.colors import SymLogNorm, LogNorm, Normalize

global edges_filename               # name of edge file
edges_filename = None
global nodes_filename             # name of node file
nodes_filename = None
global supergraph                   # the networkx supergraph
supergraph = None
global supergraph_degrees           # degrees of supergraph nodes
supergraph_degrees = None
global sum_degrees_squared          # sum of squared degrees
sum_degrees_squared = None
global n_nodes                      # number of nodes in supergraph
n_nodes = None
global n_edges                      # number of edges in supergraph
n_edges = None
global supergraph_degree_histo      # degree distribution
supergraph_degree_histo = None
global colors                       # set of colors
colors = None
global col_list                     # list of colors
col_list = None
global excluded_colors              # colors excluded from analisys
excluded_colors = ""
#excluded_colors = "ABYZ"
global pi_3                         # number of P3s
pi_3 = None
global pairs_p_3                    # set of pairs of nodes joined by a P3
pairs_p_3 = None
global node_distribution            # color distribution on nodes
node_distribution = None
global edge_distribution            # color pair distribution on edges
edge_distribution = None
global expected_edges               # expected number of edges for each pair of colors (possibly equal)
expected_edges = None
global variance_edges               # expected variance of the number of edges for each pair of colors (possibly equal)
variance_edges = None
global z_score_edges                # zscore of the number of edges for each pair of colors (possibly equal)
z_score_edges = None

def compute_graph_properties():
    global supergraph_degrees
    global n_nodes
    global n_edges
    global supergraph_degree_histo
    global col_list
    global node_distribution
    global edge_distribution
    global pi_3
    global sum_degrees_squared
    
    supergraph_degrees = nx.degree(supergraph)
    n_nodes = supergraph.number_of_nodes()
    n_edges = supergraph.number_of_edges()
    supergraph_degree_histo = nx.degree_histogram(supergraph)
# calcola numero P_3
    sum_of_squares = 0
    for grado in range(len(supergraph_degree_histo)):
        sum_of_squares += supergraph_degree_histo[grado] * grado * (grado-1)
    sum_degrees_squared = sum_of_squares
    print(f'sum of squared degrees: {sum_of_squares}')
    col_list = list(colors)
    col_list = [x for x in col_list if x not in excluded_colors]
    col_list.sort()
    node_distribution = {}
    edge_distribution = {}
    for c1 in col_list:
        edge_distribution[c1] = {}
        node_distribution[c1] = 0
        for c2 in col_list:
            edge_distribution[c1][c2] = 0
    for node in supergraph.nodes():
        c = supergraph.nodes[node]['color']
        if c not in excluded_colors:
            node_distribution[c] += 1
    for e in supergraph.edges():
        c0 = supergraph.nodes[e[0]]['color']
        c1 = supergraph.nodes[e[1]]['color']
        if c0 not in excluded_colors and c1 not in excluded_colors:
            edge_distribution[c0][c1] += 1
            if c0 != c1:
                edge_distribution[c1][c0] += 1
    pi_3 = 0
    for nodo, grado in supergraph_degrees:
        pi_3 += falling_power(grado, 2) / 2

def induced_color_subgraph(attr, val):
    '''returns the subgraph induced by nodes
where attr value is val. Returned subgraph may contain isolated nodes'''
    return supergraph.subgraph([n for n in supergraph.nodes() if supergraph.nodes[n][attr]==val]).copy()

def expected_number_singletons(grafo):
    '''computes the expected value of isolated nodes in the induced subgraph'''
    n = n_nodes
    a = grafo.number_of_nodes()
    expected = 0
    for nodo, grado in supergraph_degrees:
        expected += falling_frac(n-a, n-1, grado)
    expected *= a/n
    return expected


memo_falling_power = {}
def falling_power(x, y):
    if (x,y) not in memo_falling_power.keys():
        memo_falling_power[(x,y)] = compute_falling_power(x,y)
    return memo_falling_power[(x,y)]

def compute_falling_power(n,k):
    if k > n:
        return 0
    prod = 1
    for x in range(n, n-k, -1):
        prod *= x
    return prod
        
memo_falling_frac = {}
def falling_frac(num, den, b):
    if (num, den, b) not in memo_falling_frac:
        memo_falling_frac[(num, den, b)] = compute_falling_frac(num, den, b)
    return memo_falling_frac[(num, den, b)]

def compute_falling_frac(num, den, b):
    ''' returns falling_power(num, b)/falling_power(den, b)
    avoiding generating too large intermediate values. Assumes num <= den'''
    if b > num:
        return 0
    p = 1
    while b > 0:
        p *= num / den
        num -= 1
        den -= 1
        b -= 1
    return p
    
def neighbor_union_size(u, v):
    b = supergraph_degrees[u]
    for n in supergraph.neighbors(v):
        if not supergraph.has_edge(u, n):
            b += 1
    return b

def all_p3_pairs():
    '''builds the set of all edges (u,v) such that
    - u < v
    - u, v have a common neighbor
    - u, v are not adjacent
    '''
    global pairs_p_3
    
    if pairs_p_3 is not None:
        return
        
    profilo_gradi = supergraph_degree_histo
    pairs_p_3 = set()
    n_nodi = 0
    for nodo in nx.nodes(supergraph):
        n_nodi += 1
        if n_nodi % 10000 == 0:
            file_prog = open("progresso.txt", "a")
            print(f'   {n_nodi} nodi', file = file_prog)
            file_prog.close()
        for e in supergraph.edges(nodo):
            for f in supergraph.edges(nodo):
                u, v = e[1], f[1]
                if u >= v:
                    continue
                if not supergraph.has_edge(u, v):
                    pairs_p_3.add((u, v)) # no effect if already present
                    if len(pairs_p_3) % 10000000 == 0:
                        file_prog = open("progresso.txt", "a")
                        print(f'{len(pairs_p_3)//1000000} mln pairs', file = file_prog)
                        file_prog.close()
    
def all_pairs_contribution_rough(n, a):
    deg_hist = supergraph_degree_histo
    somma = 0
    # considera tutte le coppie come se avessero vicinati disgiunti,
    # anche coppie (u,u)
    for d1 in range(len(deg_hist)):
        if deg_hist[d1] > 0:
            for d2 in range(len(deg_hist)):
                somma += deg_hist[d1] * deg_hist[d2] * falling_frac(n-a, n-2, d1+d2)
    return somma
 
def edge_contribution_rough(n, a):
    somma = 0
    for edge in supergraph.edges():
        d1 = supergraph_degrees[edge[0]]
        d2 = supergraph_degrees[edge[1]]
        somma += falling_frac(n-a, n-2, d1+d2)
    return 2 * somma        
    
def vertices_contribution_rough(n, a):
    somma = 0
    for node in supergraph.nodes():
        d = supergraph_degrees(node)
        somma += falling_frac(n-a, n-2, 2*d)
    return somma
    
def p_3_correction(n, a):
    correction = 0
    all_p3_pairs()
    for u, v in pairs_p_3:
        correction -= falling_frac(n-a, n-2, supergraph_degrees(u)+supergraph_degrees(v))
        correction += falling_frac(n-a, n-2, neighbor_union_size(u, v))
    return 2 * correction
    
def variance_number_singletons_fast(grafo):
    n = n_nodes
    a = grafo.number_of_nodes()
    summation = 0
    summation += all_pairs_contribution_rough(n, a)
    summation -= edge_contribution_rough(n, a)
    summation -= vertices_contribution_rough(n, a)
    summation += p_3_correction(n, a)
    expected = expected_number_singletons(grafo)
    var = expected * (1 - expected) + falling_frac(a, n, 2) * summation
    return var
        
        
def z_score_number_singletons(grafo):
    '''computes the z_score of the number of isolated nodes'''
    v_fast = variance_number_singletons_fast(grafo)
    sigma = math.sqrt(v_fast)
    if sigma == 0:
        return 0
    z = (nx.degree_histogram(grafo)[0] - expected_number_singletons(grafo)) / sigma
    return z

def expected_number_edges():
    '''computes the expected value of bichromatic and monochromatic edges'''
    global expected_edges
    expected = {}
    m = n_edges
    n = n_nodes
    for c1 in col_list:
        expected[c1] = {}
    for i in range(len(col_list)):
        c1 = col_list[i]
        for j in range(i, len(col_list)):
            c2 = col_list[j]
            if c1 == c2:
                a = node_distribution[c1]
                expected[c1][c1] = m * falling_frac(a, n, 2)
            else:
                expected[c1][c2] = 2 * m * node_distribution[c1] * node_distribution[c2] / falling_power(n, 2)
                expected[c2][c1] = expected[c1][c2]
    expected_edges = expected

def variance_number_edges():
    '''computes the expected variance of the number of bichromatic and monochromatic edges'''
    global variance_edges
    variance = {}
    m = n_edges
    n = n_nodes
    n2 = falling_power(n, 2)
    n3 = falling_power(n, 3)
    n4 = falling_power(n, 4)
    for c1 in col_list:
        variance[c1] = {}
    for i in range(len(col_list)):
        c1 = col_list[i]
        for j in range(i, len(col_list)):
            c2 = col_list[j]
            if c1 == c2:
                a = node_distribution[c1]
                a2 = falling_power(a, 2)
                a3 = falling_power(a, 3)
                a4 = falling_power(a, 4)
                exp_m = m * a2 / n2
                variance[c1][c1] = exp_m - exp_m*exp_m + a4*(m*m-m)/n4 + 2*(n-a)*a3*pi_3/n4
            else:
                a = node_distribution[c1]
                b = node_distribution[c2]
                exp_m = 2 * m * a * b / n2
                term = 4 * falling_power(a, 2) * falling_power(b, 2) / n4
                variance[c1][c2] = exp_m - exp_m*exp_m + 2 * (((a * falling_power(b, 2) + falling_power(a, 2) * b) / n3 - term) * pi_3 + term * m * (m-1) / 2)
                variance[c2][c1] = variance[c1][c2]
#    print("varianza mat", variance)
    variance_edges = variance

def z_score_number_edges():
    '''computes the z_score of the number of bichromatic and monochromatic edges'''
    global z_score_edges
    expected_number_edges()
    variance_number_edges()
    z_scores = {}
    for c1 in col_list:
        z_scores[c1] = {}
    for c1 in col_list:
        for c2 in col_list:
            sigma = math.sqrt(variance_edges[c1][c2])
            if sigma == 0:
                z_scores[c1][c2] = 0
            else:
                z_scores[c1][c2] = (edge_distribution[c1][c2] - expected_edges[c1][c2]) / sigma
    z_score_edges = z_scores
#    print("z_scores", z_scores)

def print_z_scores():
    print("z_scores number of edges between colors")
    for c in col_list:
        print(c, end="    ")
    print()
    for c1 in col_list:
        print(c1, end="")
        for c2 in col_list:
            print(edges_filename + f'{z_score_edges[c1][c2]:10.3f}', end=' ')
        print()

def print_z_score_edges():
    f = open(edges_filename + "_zscores_edges.txt", "w")
    for c1 in col_list:
        for c2 in col_list:
            print(f'{edges_filename};{c1};{c2};{z_score_edges[c1][c2]:.4f}', file = f)
    f.close()
       
def subgraph_profile(grafo, color="all"):
    '''computes singleton for subgraph z_scores'''
    n_sub = grafo.number_of_nodes()
    m_sub = grafo.number_of_edges()
#    z_score_edges = z_score_number_monochromatic_edges(grafo)
    z_score_singletons = z_score_number_singletons(grafo)
    return color, n_sub, m_sub, z_score_singletons

def compute_print_z_score_singletons():
    f = open(edges_filename + "_zscores_singletons.txt", "w")
    print("color, n, m, z_score number of singletons", file = f)
    for color in col_list:
        if color not in excluded_colors:
            induced_subgraph = induced_color_subgraph('color', color)
            color, n_sub, m_sub, z_score_singletons = subgraph_profile(induced_subgraph, color)
            print(f'{edges_filename};{color};{n_sub};{m_sub};{z_score_singletons:.4f}', file = f)
    f.close()

def transform_z_score(z):
    for c1 in z:
        for c2 in z[c1]:
            z[c1][c2] = math.log(z[c1][c2] + 20)
    
def plot_heatmap():
    scores = pd.DataFrame(z_score_edges).T.fillna(0)
    fig, ax = plt.subplots(figsize=(5,5))
    
# ELIMINATO TEMPORANEAMENTE DUE RIGHE SUCCESSIVE PER PROCESSARE POKEC
#    titles = {"22491": "panel a",  "83333": "panel b",  "71421": "panel c",  "85963": "panel d",  "83332": "panel e",  "17018": "panel f",  "24327": "panel g",  "24327": "panel h",  "27284": "panel i", "4932.": "panel j"}
#    plt.title(titles[edges_filename[edges_filename.find("/")+1:edges_filename.find("/")+6]], fontsize=20)
#    sb.heatmap(scores, cmap="PiYG")
# LA RIGA SEGUENTE SERVE PER LE HEATMAPS
    sb.heatmap(scores, square=True, cmap="PiYG", vmin=2.2957, vmax=4.3957, center=2.9957, cbar=False, ax=ax)
# 
#    sb.heatmap(scores, cmap="PiYG",  norm=SymLogNorm(linthresh=0.03, linscale=0.03, vmin=-2.0, vmax=2.5))
#    plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = True, labeltop=True)
    plt.tick_params(axis='both', which='major', labelsize=12, labelleft = True, labeltop=True, left = False, right = False, labelbottom = False, bottom=False, top = False)
    plt.savefig(edges_filename+".pdf")
    print(f"saved heatmap in file {edges_filename+'.pdf'}")
    
import  sys
if  __name__ == "__main__":
    args = sys.argv
    if len(args) < 3 or len(args) > 4:
        print("Usage: python3 graphColorStatistics.py fileEdges fileColor [weight threshold]")
        exit()
    edges_filename = args[1]
    nodes_filename = args[2]
    print("===============")
    print("Files: "+edges_filename+", "+nodes_filename)
    if  len(args) == 4:
        weight_threshold = int(args[3])
    else:
        weight_threshold = 700
# create supergraph
    supergraph = nx.Graph()
    supergraph.graph["name"] = edges_filename
    colors = set()
    colorGroups = set()
    readGraph.inputGraphFromFile(nodes_filename, edges_filename, supergraph, colors, colorGroups, weight_threshold, isolated=False)

    duration = 0
    start = time.time()
    compute_graph_properties()
    print(f'graph with {n_nodes} nodes and {n_edges} edges')
#    dens_tot = density(supergraph)
    z_score_number_edges()	
    duration += time.time()-start
    print(f'{edges_filename}: {duration} seconds for computing edge z-scores')
    print_z_score_edges()

# z_score log transformation for plotting heatmap
    transform_z_score(z_score_edges)
# plot heatmap
    plot_heatmap()
    start = time.time()
    compute_print_z_score_singletons()
    duration += time.time()-start
    print(f'{edges_filename}: {duration} seconds for computing singleton z-scores')

       
