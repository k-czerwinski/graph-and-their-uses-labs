from graphic_sequence.utils import is_graphic_sequence
import networkx as nx
import matplotlib.pyplot as plt
from graph_drawing.utils import *

file_path = 'sample_data/graphic_sequence.txt'

with open(file_path, 'r') as file:
    sequence = list(map(int, file.readline().split()))
    print(sequence)
    is_graphic_seq = is_graphic_sequence(sequence)
    print("Is graphic sequence? " + str(is_graphic_seq))
    if(is_graphic_seq):
        sequence = sorted(sequence)
        G = nx.havel_hakimi_graph(sequence)
        G = rename_nodes_labels(G)
        nx.draw_circular(G, with_labels=True)
        plt.show()
