from graphic_sequence.utils import is_graphic_sequence, construct_graph_from_sequence, randomize_graph
import matplotlib.pyplot as plt
import networkx as nx

sequence = [2,2,2,6]

print(is_graphic_sequence(sequence))
G = construct_graph_from_sequence(sequence)
nx.draw_circular(G,with_labels=True)
plt.show()