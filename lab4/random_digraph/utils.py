import random
from itertools import permutations
import numpy as np
import networkx as nx
from matplotlib import pyplot as plt

def generate_random_digraph_with_edge_probability(number_of_nodes, edge_exist_probability):
    if number_of_nodes <= 0:
        raise ValueError("Number of nodes must be greater than 0.")
    if edge_exist_probability < 0 or edge_exist_probability > 1:
        raise ValueError("Probability of an edge existance must be between 0 and 1")
    adjacency_matrix = np.zeros((number_of_nodes, number_of_nodes))
    all_perm = permutations(range(number_of_nodes), 2) # without loops
    count = 0
    for v1, v2 in all_perm:
        if random.choices([True, False], weights=[edge_exist_probability, 1 - edge_exist_probability])[0]:
            adjacency_matrix[v1-1][v2-1] = 1
            count+=1
    print(f"Number of edges: {count}")
    return adjacency_matrix

def generate_random_weights(adjacency_matrix):
    G = nx.DiGraph(adjacency_matrix)
    weights = {edge: random.randint(-5, 10) for edge in G.edges}
    nx.set_edge_attributes(G, weights, 'weight')
    # plt.figure()
    # plt.clf()
    
    # elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    # esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
    # pos = nx.spring_layout(G, seed=7)
    
    # nx.draw_networkx_nodes(G, pos, node_size=700)
    
    # # edges
    # nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    # nx.draw_networkx_edges(
    #     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    # )

    # # node labels
    # nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # # edge weight labels
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels)
    # ax = plt.gca()
    # ax.margins(0.08)
    # plt.axis("off")
    # plt.tight_layout()
    # plt.show()
    return G, weights