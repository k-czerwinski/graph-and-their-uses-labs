import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

def rename_nodes_labels(G:nx.Graph):
        mapping = {node: node + 1 for node in G.nodes()}
        G = nx.relabel_nodes(G, mapping)
        return G

def draw_digraph_from_adjacency_matrix(adjacency_matrix:np.matrix, filename:str):
        plt.figure()
        G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
        G = rename_nodes_labels(G)
        nx.draw(G, with_labels=True)
        plt.savefig(filename)