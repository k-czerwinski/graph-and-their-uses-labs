
import networkx as nx
import matplotlib.pyplot as plt  
from WeightEdgesGraph import WeightEdgesGraph, GraphRepresentation

# Example usage:
file_path = "sample_data/weight_adjacency_matrix.txt"

# Create WeightEdgesGraph instance and read the weight matrix from the file
graph = WeightEdgesGraph(file_path)

# Get the graph for NetworkX visualization
G = graph.get_graph_for_networkx()

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
