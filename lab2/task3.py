from graphic_sequence.utils import is_graphic_sequence, construct_graph_from_sequence, randomize_graph
import networkx as nx
import matplotlib.pyplot as plt
from graph_drawing.utils import *
from consistent_graph.utils import components, largest_connected_component, color_map

file_path = 'sample_data/graphic_sequence.txt'

with open(file_path, 'r') as file:
    sequence = list(map(int, file.readline().split()))
    print(sequence)
    is_graphic_seq = is_graphic_sequence(sequence)
    print("Is graphic sequence? " + str(is_graphic_seq))
    G = construct_graph_from_sequence(sequence)
    G = randomize_graph(G)
    comp = components(G)
    print("Components: " + str(comp))
    LargestConnectedComponent = largest_connected_component(G)
    print("Largest connected component: " + str(LargestConnectedComponent))
    plt.clf()
    nx.draw_circular(G, node_color = color_map(comp) ,with_labels=True)
    plt.savefig('../target/graph_with_component.png')