import networkx as nx
from graphic_sequence.utils import randomize_graph, construct_graph_from_sequence

def generate_random_k_regular_graph(n, k) -> nx.Graph:
    if k >= n:
        raise ValueError("k must be less than n")
    if k % 2 == 1 and n % 2 == 1:
        raise ValueError("n must be even if k is odd")
    sequence = [k for _ in range(n)]
    graph = construct_graph_from_sequence(sequence)
    return randomize_graph(graph)