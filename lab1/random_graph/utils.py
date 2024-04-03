import random
from itertools import combinations
from random import sample
import numpy as np

def generate_random_graph(number_of_nodes, number_of_edges):
    if number_of_nodes <= 0:
        raise ValueError ("Number of nodes must be greater than 0.")
    if number_of_edges > number_of_nodes * (number_of_nodes - 1) / 2:
        raise ValueError ("Number of edges must be smaller than n * (n-1) / 2, where n is the number of nodes. ")
    if number_of_edges < 0:
        raise ValueError("Number of edges must be non negative number")

    adjacency_matrix = np.zeros((number_of_nodes, number_of_nodes))
    all_comb = combinations(range(number_of_nodes), 2)
    for v1, v2 in sample(list(all_comb), k=number_of_edges):
        adjacency_matrix[v1-1][v2-1] = 1
        adjacency_matrix[v2-1][v1-1] = 1
        print('{}->{}'.format(v1, v2))
    print(adjacency_matrix)
    return adjacency_matrix

def generate_random_graph_with_edge_probability(number_of_nodes, edge_exist_probability):
    if number_of_nodes <= 0:
        raise ValueError("Number of nodes must be greater than 0.")
    if edge_exist_probability < 0 or edge_exist_probability > 1:
        raise ValueError("Probability of an edge existance must be between 0 and 1")
    adjacency_matrix = np.zeros((number_of_nodes, number_of_nodes))
    all_comb = combinations(range(number_of_nodes), 2)
    count = 0
    for v1, v2 in all_comb:
        if random.choices([True, False], weights=[edge_exist_probability, 1 - edge_exist_probability])[0]:
            adjacency_matrix[v1-1][v2-1] = 1
            adjacency_matrix[v2-1][v1-1] = 1
            count+=1
    print(f"Number of edges: {count}")
    return adjacency_matrix