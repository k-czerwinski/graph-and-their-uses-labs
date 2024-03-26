from euler_graph.utils import generate_random_euler_graph, find_euler_cycle
from graphic_sequence.utils import is_graphic_sequence, construct_graph_from_sequence, randomize_graph
import matplotlib.pyplot as plt
import networkx as nx

sequence = generate_random_euler_graph(8)
G = construct_graph_from_sequence(sequence)
nx.draw_circular(G,with_labels=True)
plt.savefig('target/euler_graph.png')
print(find_euler_cycle(G))
