from graphic_sequence.utils import is_graphic_sequence, construct_graph_from_sequence, randomize_graph
from consistent_graph.utils import components, largest_connected_component, color_map
from euler_graph.utils import generate_random_euler_graph, find_euler_cycle
from k_regular_graph.utils import generate_random_k_regular_graph
from hamilton_graph.utils import is_hamiltonian
import networkx as nx
import matplotlib.pyplot as plt
import sys
import os

current_dir = os.path.dirname(__file__)

parent_dir = os.path.dirname(current_dir)

sys.path.append(parent_dir)
from lab1.random_graph.utils import generate_random_graph

file_path = 'lab2/sample_data/graphic_sequence.txt'

# task 6
print("Task 6")
number_of_nodes = int(input("Enter number of nodes: "))
node_of_edges = int(input("Enter edges: "))
G = nx.Graph(generate_random_graph(number_of_nodes, node_of_edges))
plt.clf()
nx.draw_circular(G,with_labels=True)
plt.savefig('random_graph.png')
hamiltonian, path = is_hamiltonian(G)
if hamiltonian:
    path.append(path[0])
print(hamiltonian, path)