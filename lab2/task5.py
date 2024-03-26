import networkx as nx
from k_regular_graph.utils import generate_random_k_regular_graph
from graphic_sequence.utils import construct_graph_from_sequence, randomize_graph
import matplotlib.pyplot as plt

G = generate_random_k_regular_graph(7, 2)
nx.draw_circular(G, with_labels=True)
plt.savefig('target/k_regular_graph.png')