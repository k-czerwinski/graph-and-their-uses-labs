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

# task 1
print("Task 1")
print("Enter graphic sequence: ")
sequence = list(map(int, input().split()))
print(sequence)
is_graphic_seq = is_graphic_sequence(sequence)
print("Is graphic sequence? " + str(is_graphic_seq))
G = construct_graph_from_sequence(sequence)
nx.draw_circular(G, with_labels=True)
plt.savefig('graph_from_sequence.png')

# task 2
print("Task 2")
number_of_randomizations = int(input("Enter number of randomizations: "))
G = randomize_graph(G, number_of_randomizations)
plt.clf()
nx.draw_circular(G, with_labels=True)
plt.savefig('graph_from_sequence_randomize.png')

# task 3
print("Task 3")
comp = components(G)
print("Components: " + str(comp))
LargestConnectedComponent = largest_connected_component(G)
print("Largest connected component: " + str(LargestConnectedComponent))
plt.clf()
nx.draw_circular(G, node_color = color_map(comp) ,with_labels=True)
plt.savefig('graph_with_component.png')
