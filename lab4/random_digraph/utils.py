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
    weights = {edge: random.randint(0, 20) for edge in G.edges}
    nx.set_edge_attributes(G, weights, 'weight')
    return G, weights