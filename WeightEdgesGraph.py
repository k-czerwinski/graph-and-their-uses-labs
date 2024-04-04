import numpy as np
from SimpleGraph import SimpleGraph, GraphRepresentation

class WeightEdgesGraph(SimpleGraph):
    def __init__(self, input_array, graph_representation):
        super().__init__(input_array, graph_representation)
        self.WEIGHT_MATRIX = np.zeros_like(self.array, dtype=int)
        self.distance_matrix = None
        for i in range(len(input_array)):
            for j in range(i,len(input_array[i])):
                if input_array[i][j] == 1:
                    self.WEIGHT_MATRIX[j][i] = self.WEIGHT_MATRIX[i][j] = np.random.randint(1, 10)

    def add_weights(self, weight_matrix):
        if not isinstance(weight_matrix, np.ndarray):
            raise TypeError("Weight matrix must be a NumPy array")
        if weight_matrix.shape != self.array.shape:
            raise ValueError("Weight matrix must have the same shape as the input array")
        
        self.WEIGHT_MATRIX = weight_matrix

    def get_weight_matrix(self):
        if self.WEIGHT_MATRIX is not None:
            return self.WEIGHT_MATRIX
        else:
            return np.zeros_like(self.array, dtype=int)

    def dijkstra_shortest_path(self, source):
        if self.graph_representation != GraphRepresentation.NEIGHBOURHOOD_MATRIX:
            raise ValueError("Dijkstra's algorithm requires the graph to be represented as a neighbourhood matrix.")
        
        num_vertices = len(self.array)
        dist = [float('inf')] * num_vertices
        dist[source] = 0
        visited = [False] * num_vertices

        for _ in range(num_vertices):
            u = self.__min_distance_vertex(dist, visited)
            visited[u] = True

            for v in range(num_vertices):
                if self.array[u][v] and visited[v] == False and dist[v] > dist[u] + self.WEIGHT_MATRIX[u][v]:
                    dist[v] = dist[u] + self.WEIGHT_MATRIX[u][v]

        return dist

    def compute_distance_matrix(self):
        if self.graph_representation != GraphRepresentation.NEIGHBOURHOOD_MATRIX:
            raise ValueError("Distance matrix computation requires the graph to be represented as a neighbourhood matrix.")
        
        num_vertices = len(self.array)
        distance_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

        for i in range(num_vertices):
            shortest_distances = self.dijkstra_shortest_path(i)
            distance_matrix[i] = shortest_distances

        self.distance_matrix = distance_matrix  # Store the distance matrix
        return distance_matrix

    def find_center(self):
        if self.distance_matrix is None:
            self.compute_distance_matrix()

        total_distances = np.sum(self.distance_matrix, axis=1)
        center_index = np.argmin(total_distances)
        return center_index

    def find_minimax_center(self):
        if self.distance_matrix is None:
            self.compute_distance_matrix()

        max_distances = np.max(self.distance_matrix, axis=1)
        minimax_center_index = np.argmin(max_distances)
        return minimax_center_index

    def __min_distance_vertex(self, dist, visited):
        min_dist = float('inf')
        min_vertex = -1
        for v in range(len(dist)):
            if dist[v] < min_dist and visited[v] == False:
                min_dist = dist[v]
                min_vertex = v
        return min_vertex

# Example usage:
file_path = "sample_data/adjacency_matrix.txt"
adjacency_list = SimpleGraph.load_adjacency_list(file_path)
graph = WeightEdgesGraph(adjacency_list, GraphRepresentation.NEIGHBOURHOOD_MATRIX)

# Find the center of the graph
center_index = graph.find_center()
print("Center of the graph:", center_index)

# Find the minimax center of the graph
minimax_center_index = graph.find_minimax_center()
print("Minimax center of the graph:", minimax_center_index)
