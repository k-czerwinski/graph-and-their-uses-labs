import networkx as nx
from random_graph.utils import generate_random_graph
from hamilton_graph.utils import is_hamiltonian
import matplotlib.pyplot as plt

G = nx.Graph(generate_random_graph(7, 10))
nx.draw_circular(G,with_labels=True)
plt.savefig('graph-and-their-uses-labs/target/random_graph.png')
hamiltonian, path = is_hamiltonian(G)
if hamiltonian:
    path.append(path[0])
print(hamiltonian, path)
