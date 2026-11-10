# aggiunto parametro "--color_position", default 2, per poter interpretare
# un campo in posizione variabile nel file dei nodi come specifica del colore

# eliminato processing del nome dei nodi, lasciato solo lo strip

__authors__ = ("Paolo Giulio Franciosa (paolo.franciosa@uniroma1.it)",
               "Nicola Apollonio (nicola.apollonio@cnr.it)",
               "Daniele Santoni (daniele.santoni@iasi.cnr.it)")

__version__ = "0.1.1"
__date__ = "Sept 8, 2023"

import sys

# Define tool name
TOOL_ID="honto_streaming"

# Control current Python version
# It requires Python 3 or higher
if sys.version_info[0] < 3:
    raise Exception("f{TOOL_ID} requires Python 3, your current Python version is {sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}")

''' computes homophily and heterophily z-scores as described in article
Apollonio, Franciosa, Santoni
Evaluating homophily/heterophily of weighted networks through second-order statistics in a data streaming setting

The network is expected to be provided in two text files:

nodes_file:
XXX ... CCC ... on each line, where XXX is a node label (string)
                      and CCC is its color (string),
                      separated by spaces. If parameter --color_position is given,
                      field CCC is taken from a different position

edges_file:
XXX YYY WWW on each line, where XXX and YYY are node labels,
                          WWW is the edge weight as an int or float number
                          with possibly a decimal point
                          separated by spaces

z-scores are written, one line per each color pair, in a text file with name
nodes_file + ".weighted_zscores.txt"

ASSUMPTIONS:
- each edge appears twice in edges_file, as (x, y) and (y, x), with the same weight,
  unless parameter --no_symmetric is given
'''

import math
import argparse as ap
import os

def read_params():
    p = ap.ArgumentParser( description = ( "Measuring homophily/heterophily in weighted networks" ),
                           formatter_class = ap.ArgumentDefaultsHelpFormatter )
    # Inputs
    p.add_argument( '--input_edges', 
                    type = str,
                    help = "Path to the file with the list of edges" )
    p.add_argument( '--input_nodes', 
                    type = str,
                    help = "Path to the file with nodes and colors" )
    p.add_argument( '--color_position',
                    type = int,
                    default = 2,
                    help = "field in node file to be considered as color. Input fields are separated by spaces" )
    p.add_argument( '--no_symmetric',
                    action = 'store_true',
                    default = False,
                    help = "edges are not repeated as symmetric pairs in input file" )
    p.add_argument( '--isolated',
                    action = 'store_true',
                    default = False,
                    help = "Maintain isolated nodes" )
    p.add_argument( '--overwrite',
                    action = 'store_true',
                    default = False,
                    help = "Overwrite results if already exist" )
    p.add_argument( '--verbose',
                    action = 'store_true',
                    default = False,
                    help = "Print results in real time" )
    p.add_argument( '-v', 
                    '--version', 
                    action = 'version',
                    version = '{} v{} ({})'.format( TOOL_ID, __version__, __date__ ),
                    help = f"Print current {TOOL_ID} version and exit")
    return p.parse_args()

def scan_node_line(node_color, color_position):
    '''returns the node name and color.
Color is returned as "_blank" if it is not present'''
    fields = node_color.split()
    node = fields[0].strip()
    color = fields[color_position - 1].rstrip() if len(fields) >= color_position else "_blank"
    return node, color


def falling(n, e):
    '''returns the falling power n^e. Retuns 0 if n < e'''
    if n < e:
        return 0
    res = 1
    for i in range(e):
        res *= n
        n -= 1
    return res

def print_tab_i_j(var, message, file_out_name = None):
    if file_out_name is not None:
        file_out = open(file_out_name, "w")
    else:
        file_out = None
    print("\n", message, file = file_out)
    print(f'{" ":11s}', end="", file = file_out)
    for i in sorted(var.keys()):
        print(f'{i:^11s}', end="", file = file_out)
    print(file = file_out)
    for i in sorted(var.keys()):
        print(f'{i:^11s}', end="", file = file_out)
        for j in sorted(var.keys()):
            print(f'{var[i][j]:11.2f}', end="", file = file_out)
        print(file = file_out)
    if file_out_name is not None:
        file_out.close()
    
def print_in_line_i_j(var, message, file_name, file_out_name = None):
    if file_out_name is not None:
        file_out = open(file_out_name, "w")
    else:
        file_out = None
    for i in sorted(var.keys()):
        print(f'', end="", file = file_out)
        for j in sorted(var.keys()):
            print(f'{file_name};{i};{j};{var[i][j]:.4f}', file = file_out)
    if file_out_name is not None:
        file_out.close()
    
class GraphHomophily:
    def __init__(self):
        self.__n       = 0
        self.__m       = 0  # is temporarily twice the real value. To be halved after edge read
        self.__w_sum   = 0  # is temporarily twice the real value. To be halved after edge read
        self.__w_2_sum = 0  # is temporarily twice the real value. To be halved after edge read
        self.__P_3_sum = 0
        self.__profile = dict()  #  for each color: number of nodes
        self.__edge_profile = dict() # for each col1: for each col2: number of edges (symmetric)
        self.__node_color = dict()   # for each node: color
        self.__node_degree = dict()   # for each node: its degree
        self.__node_local_w = dict() # for each node: sum of weights of incident edges
        self.__node_local_P_3 = dict() # for each node: sum of weights of P_3's centered in node

    def __str__(self):
       s = f'''
        n: {self.__n}
        m: {self.__m}
        w_sum: {self.__w_sum}
        w_2_sum: {self.__w_2_sum}
        P_3_sum: {self.__P_3_sum}
        profile: {self.__profile}
        edge_profile: {self.__edge_profile}
        node_color: {self.__node_color}
        node_local_w: {self.__node_local_w}
        node_local_P_3: {self.__node_local_P_3}
        P_3_sum: {self.__P_3_sum}
'''
       return s 
        
    def print_profile(self):
        s = f'''
        n: {self.__n}
        m: {self.__m}
        profile: {self.__profile}
        w_sum: {self.__w_sum}
        w_2_sum: {self.__w_2_sum}
        P_3_sum: {self.__P_3_sum}
'''
        print(s)

    def add_node(self, node, color = None):
        '''adds a node to dicts __node_color and __node_degree, if it does not exist'''
        if node not in self.__node_color: # first occurrence of node
            self.__n += 1
            self.__node_color[node] = color
            self.__node_degree[node] = 0
            self.__profile[color] = self.__profile.get(color, 0) + 1
            self.__node_local_w[node] = 0
            self.__node_local_P_3[node] = 0
        if color not in self.__edge_profile: # first occurrence of color
            for c in self.__edge_profile:
                self.__edge_profile[c][color] = 0
            self.__edge_profile[color] = dict()
            for c in self.__edge_profile:
                self.__edge_profile[color][c] = 0
           

    def add_edge(self, n1, n2, weight):
        '''updates graph status by considering an edge.
        If nodes n1, n2 or both do not exist, also adds nodes to
        dicts __node_color and __node_degree
        '''
        node1, color1 = n1, "_blank"
        if node1 not in self.__node_color:
            self.add_node(node1, color1)
        color1 = self.__node_color[node1]
        node2, color2 = n2, "_blank"
        if node2 not in self.__node_color:
            self.add_node(node2, color2)
        color2 = self.__node_color[node2]
        self.__m += 1
        self.__node_degree[node1] += 1
        self.__w_sum += weight
        self.__w_2_sum += weight * weight
        self.__edge_profile[color1][color2] += weight
        self.__node_local_P_3[node1] += weight * self.__node_local_w[node1]
        self.__node_local_w[node1] += weight


    def read_graph(self, nodes_filename, color_position, edges_filename, symmetric, isolated):
        '''reads a weighted graph in the following form:

nodes_file:
XXX ... CCC ... on each line, where XXX is a node label and CCC is its color
color is specified in position color_position, counting from position 1. So default is color_position 2 if line format is just XXX CCC

edges_file:
XXX YYY WWW on each line, where XXX and YYY are node labels,
                          WWW is the edge weight as an int or float number
                          with possibly a decimal point

and returns:
- number of nodes
- number of edges
- node distribution (profile) as a dict {color: number_of_nodes, ...}
- edge distribution (edge_profile) as a dict of dict giving the sum of weights of i-i and i-j edges
- sum of edge weights
- sum of squares of edge weights
- sum of weight products for P_3's
'''
        try:
            f_nodes = open(nodes_filename)
            f_edges = open(edges_filename)
            for node_row in f_nodes:
                node, color = scan_node_line(node_row, color_position)
                self.add_node(node, color)
            for edge_row in f_edges:
                n1, n2, weight = edge_row.split()
                weight = float(weight)
                self.add_edge(n1, n2, weight)
                if not symmetric:
                    self.add_edge(n2, n1, weight)
            self.__m //= 2
            self.__w_sum /= 2
            self.__w_2_sum /= 2
            self.__P_3_sum = sum(self.__node_local_P_3.values())
            for c in self.__edge_profile:
                self.__edge_profile[c][c] /= 2
            if not isolated:
                for n in self.__node_degree:
                    if self.__node_degree[n] == 0:
                        self.__n -= 1
                        col = self.__node_color.pop(n)
                        self.__profile[col] -= 1
                        self.__node_local_w.pop(n)
                        self.__node_local_P_3.pop(n)
                for c in self.__profile:
                    if self.__profile[c] == 0:
                        self.__profile.pop(c)
                        self.__edge_profile.pop(c, 0)
                        for c1 in self.__edge_profile:
                            self.__edge_profile[c1].pop(c, 0)
                    
        except:
            print("error in opening and reading files")
        
    def compute_exp_var_all_i_j(self):
        '''returns Exp(M^i,j) and Var(M^i,j) for all pairs of colors i,j as a dict'''
        profile = self.__profile
        n = self.__n
        w_sum = self.__w_sum
        w_2_sum = self.__w_2_sum
        P_3_sum = self.__P_3_sum
        expected = dict()
        variance = dict()
        n_2 = falling(n, 2)
        n_3 = falling(n, 3)
        n_4 = falling(n, 4)
        for color_i in sorted(profile.keys()):
            expected[color_i] = dict()
            variance[color_i] = dict()
            ci = profile[color_i]
            ci_2 = falling(ci, 2)
            ci_3 = falling(ci, 3)
            ci_4 = falling(ci, 4)
            for color_j in sorted(profile.keys()):
                cj = profile[color_j]
                cj_2 = falling(cj, 2)
                cj_3 = falling(cj, 3)
                cj_4 = falling(cj, 4)
                if color_j != color_i:
                    expected[color_i][color_j] = 2*ci*cj/n_2*w_sum
                    variance[color_i][color_j] = \
                             2*ci*cj/n_2*w_2_sum - 4*(ci*cj/n_2*w_sum)**2 \
                            + 2*((ci*cj_2+ci_2*cj)/n_3 - 4*ci_2*cj_2/n_4)*P_3_sum \
                            + 4*ci_2*cj_2/n_4*(w_sum**2-w_2_sum)
                else: # color_i == color_j
                    expected[color_i][color_i] = ci_2/n_2*w_sum
                    variance[color_i][color_i] = \
                             ci_2/n_2*w_2_sum \
                            - (ci_2/n_2*w_sum)**2 + 2*(ci_3/n_3-ci_4/n_4)*P_3_sum \
                            + ci_4/n_4*(w_sum**2-w_2_sum)
        return expected, variance
    
    def compute_z_scores_i(edge_profile, exp_i, sigma_i):
        '''returns a dict representing the z_scores of M_i'''
        z_score_i = {k: (edge_profile[k][k] - exp_i[k]) / sigma_i[k] for k in exp_i}
        return z_score_i
    
    def compute_z_scores_i_j(self, exp_ij, sigma_ij):
        '''returns a dict of dicts representing the z_scores of M_i,j'''
    #    z_score_i_j = {k1: {k2: (edge_profile[k1][k2] - exp_ij[k1][k2]) / sigma_ij[k1][k2] for k2 in exp_ij[k1]} for k1 in exp_ij}
        z_score_i_j = {k1: {k2: (self.__edge_profile[k1][k2] - exp_ij[k1][k2]) / sigma_ij[k1][k2] if sigma_ij[k1][k2] != 0 else 0 for k2 in exp_ij[k1]} for k1 in exp_ij}
        return z_score_i_j
        
def compute_print_homophily(node_file, color_position, edge_file, out_file_name, symmetric, isolated, verbose):
    g = GraphHomophily()
    g.read_graph(node_file, color_position, edge_file, symmetric, isolated)
    if verbose:
        print(f'node_file: {node_file}\nedge_file: {edge_file}')
        print(f'z_scores are written in {out_file_name} ... ', end = "")
        g.print_profile()
    
#    print_tab_i_j(edge_profile, "edge_profile")
    exp_ij, var_ij = g.compute_exp_var_all_i_j()
#    print_tab_i_j(exp_ij, "expected_i,j")
#    print_tab_i_j(var_ij, "variance_i,j")
    sigma_ij = {k1: {k2: math.sqrt(var_ij[k1][k2]) for k2 in var_ij[k1]} for k1 in var_ij}
#    print_tab_i_j(sigma_ij, "sigma_i,j")
    z_score_ij = g.compute_z_scores_i_j(exp_ij, sigma_ij)
#    print_tab_i_j(z_score_ij, "z_score_i,j")
    print_in_line_i_j(z_score_ij, "z_score_i,j", edge_file, file_out_name = out_file_name)
    if verbose:
        print("done")
    
if __name__ == "__main__":
    args = read_params()
    if not args.input_edges or not os.path.exists(args.input_edges):
        print('type "python3 weightedHomophilyStreaming.py  -h"  for help')
        raise FileNotFoundError(f"Unable to locate input file: {args.input_edges}")
    # input_nodes is optional
    if args.input_nodes and not os.path.exists(args.input_nodes):
        raise FileNotFoundError(f"Unable to locate input file: {args.input_nodes}")
    out_file_name = args.input_edges+".weighted_zscores.txt"
    if  not args.overwrite and os.path.exists(out_file_name):
                raise OSError(f"Output file already exists: {out_file_name}")

    compute_print_homophily(args.input_nodes, args.color_position, args.input_edges, out_file_name, not args.no_symmetric, args.isolated, args.verbose)
