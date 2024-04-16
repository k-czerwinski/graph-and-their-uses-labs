import networkx as nx
import matplotlib.pyplot as plt
from WeightEdgesGraph import WeightEdgesGraph, GraphRepresentation

# Example usage:
file_path = "lab3/sample_data/weight_adjacency_matrix.txt"

# Create WeightEdgesGraph instance and read the weight matrix from the file
graph = WeightEdgesGraph(file_path)

# Define starting vertex
start_vertex = 1


# Compute shortest paths from the starting vertex
shortest_distances, shortest_paths = graph.dijkstra_shortest_path(start_vertex)

# Print the results in the specified format
print(f"START: s = {start_vertex}")
for i, dist in enumerate(shortest_distances):
    if i == start_vertex - 1:
        print(f"d({i+1}) = 0 ==> [{i+1}]")
    else:
        path = shortest_paths[i]
        path.append(i + 1)
        print(f"d({i+1}) = {dist} ==> {path}")


