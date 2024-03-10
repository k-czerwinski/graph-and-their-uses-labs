import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def rename_nodes_labels(G:nx.Graph):
        mapping = {node: node + 1 for node in G.nodes()}
        G = nx.relabel_nodes(G, mapping)
        return G

def draw_graph_on_circle_from_adjacency_matrix(adjacency_matrix:np.matrix):
        G = nx.from_numpy_array(adjacency_matrix)
        G = rename_nodes_labels(G)
        nx.draw_circular(G, with_labels=True)
        plt.savefig('./target/graph.png')