from graphic_sequence.utils import is_graphic_sequence, construct_graph_from_sequence, randomize_graph
import networkx as nx
import matplotlib.pyplot as plt
from graph_drawing.utils import *

file_path = 'sample_data/graphic_sequence.txt'

with open(file_path, 'r') as file:
    sequence = list(map(int, file.readline().split()))
    print(sequence)
    is_graphic_seq = is_graphic_sequence(sequence)
    print("Is graphic sequence? " + str(is_graphic_seq))
    G = construct_graph_from_sequence(sequence)
    G = rename_nodes_labels(G)
    nx.draw_circular(G, with_labels=True)
    plt.savefig('../target/graph_from_sequence.png')
    G = randomize_graph(G,7)
    plt.clf()
    nx.draw_circular(G, with_labels=True)
    plt.savefig('../target/graph_from_sequence_randomize.png')