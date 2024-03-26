import networkx as nx
import matplotlib.pyplot as plt
from graphic_sequence.utils import construct_graph_from_sequence, is_graphic_sequence, randomize_graph
import random

def generate_random_euler_graph(n) -> nx.Graph:
    while True:
        sequence = [random.randint(0, 2*n) for _ in range(n)]
        if is_graphic_sequence(sequence) and is_eulerian(sequence):
            break
    return sequence

def is_eulerian(sequence):
    return all([x % 2 == 0 and x != 0 for x in sequence])
    
def find_euler_cycle(graph: nx.Graph):
    return list(nx.eulerian_circuit(graph))