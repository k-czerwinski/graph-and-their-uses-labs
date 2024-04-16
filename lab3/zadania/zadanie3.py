import numpy as np
from WeightEdgesGraph import WeightEdgesGraph, GraphRepresentation


# Utwórz instancję klasy WeightEdgesGraph z pliku
file_path = "sample_data/weight_adjacency_matrix.txt"
graph = WeightEdgesGraph(file_path)

# Oblicz macierz odległości
distance_matrix = graph.compute_distance_matrix()

# Wyświetl macierz odległości
print("Macierz odległości:")
print(distance_matrix)
