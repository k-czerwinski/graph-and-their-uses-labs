import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

def rename_nodes_labels(G: nx.Graph):
    mapping = {node: node + 1 for node in G.nodes()}
    G = nx.relabel_nodes(G, mapping)
    return G

def draw_digraph_from_adjacency_matrix(adjacency_matrix: np.matrix, filename: str):
    plt.figure()
    G = nx.from_numpy_array(adjacency_matrix, create_using=nx.DiGraph)
    G = rename_nodes_labels(G)
    pos = nx.spring_layout(G)  # Use spring layout for better positioning
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=12, font_weight='bold', edge_color='black')
    plt.savefig(filename)
    plt.close()

def draw_graph_with_weights(G: nx.Graph, weights: dict, filename: str):
    plt.figure()
    pos = nx.spring_layout(G)  # Use spring layout for better positioning
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=12, font_weight='bold', edge_color='black', arrows=True)
    edge_labels = {(u, v): f'{w}' for u, v, w in G.edges(data=True) if w}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=10, font_color='red')
    plt.savefig(filename)
    plt.close()
