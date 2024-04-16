import networkx as nx
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
    start_vertex = random.choice(list(graph.nodes))
    current_vertex = start_vertex
    euler_cycle = []
    while graph.edges:
        neighbors = list(graph.neighbors(current_vertex))
        if neighbors:
            next_vertex = random.choice(neighbors)
            graph.remove_edge(current_vertex, next_vertex)
            if len(graph[current_vertex]) == 0:
                graph.remove_node(current_vertex)
            euler_cycle.append((current_vertex, next_vertex))
            current_vertex = next_vertex
        else:
            break
    return euler_cycle