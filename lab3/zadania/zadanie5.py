import networkx as nx
import matplotlib.pyplot as plt
from WeightEdgesGraph import WeightEdgesGraph, GraphRepresentation

# Ścieżka do pliku z macierzą wag
file_path = "sample_data/weight_adjacency_matrix.txt"

# Utworzenie instancji klasy WeightEdgesGraph na podstawie pliku z macierzą wag
graph = WeightEdgesGraph(file_path)



# Get the graph for NetworkX visualization
G = graph.get_graph_for_networkx()

print(graph.array)


# Obliczenie minimalnego drzewa rozpinającego za pomocą metody kruskal_minimum_spanning_tree()
mst = graph.kruskal_minimum_spanning_tree()

# Wizualizacja minimalnego drzewa rozpinającego
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(mst)
nx.draw(mst, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
plt.title("Minimalne drzewo rozpinające")
plt.show()
