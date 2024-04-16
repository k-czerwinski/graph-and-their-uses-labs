from WeightEdgesGraph import WeightEdgesGraph, GraphRepresentation
import numpy as np

file_path = "sample_data/weight_adjacency_matrix.txt"
graph = WeightEdgesGraph(file_path)

# Znajdź centrum grafu
center_vertex = graph.find_center()

# Znajdź centrum minimax grafu
minimax_center_vertex = graph.find_minimax_center()

# Oblicz sumę odległości dla centrum
sum_of_distances = np.sum(graph.compute_distance_matrix()[center_vertex])

# Oblicz odległość od najdalszego wierzchołka dla centrum minimax
max_distance_from_center = np.max(graph.compute_distance_matrix()[minimax_center_vertex])

# Wyświetl wyniki
print("Centrum =", center_vertex + 1, "(suma odległości:", sum_of_distances, ")")
print("Centrum minimax =", minimax_center_vertex + 1, "(odległość od najdalszego:", max_distance_from_center, ")")
