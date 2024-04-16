import networkx as nx
import numpy as np
import matplotlib.pyplot as plt  
from SimpleGraph import SimpleGraph, GraphRepresentation
import heapq

class WeightEdgesGraph(SimpleGraph):
    def __init__(self, input_data, representation_type=None):
        if isinstance(input_data, str):
            # Read data from file if input is a file path
            self.WEIGHT_MATRIX = self.__read_weight_matrix(input_data)
        elif isinstance(input_data, np.ndarray):
            # Directly assign input data
            self.WEIGHT_MATRIX = input_data
        else:
            raise TypeError("Input data must be either a file path or a NumPy array")
        
        if representation_type is not None:
            super().__init__(self.WEIGHT_MATRIX, representation_type)
        else:
            super().__init__(self.WEIGHT_MATRIX, GraphRepresentation.NEIGHBOURHOOD_MATRIX)
        
        self.distance_matrix = None

    def __read_weight_matrix(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            weight_matrix = []
            for line in lines:
                weights = list(map(int, line.split()))
                weight_matrix.append(weights)
        return np.array(weight_matrix)

    def add_weights(self, weight_matrix):
        if not isinstance(weight_matrix, np.ndarray):
            raise TypeError("Weight matrix must be a NumPy array")
        if weight_matrix.shape != self.WEIGHT_MATRIX.shape:
            raise ValueError("Weight matrix must have the same shape as the input array")
        
        self.WEIGHT_MATRIX = weight_matrix

    def dijkstra_shortest_path(self, source):
        num_vertices = len(self.WEIGHT_MATRIX)
        dist = [float('inf')] * num_vertices
        paths = [[] for _ in range(num_vertices)]
        dist[source - 1] = 0
        visited = set()

        while len(visited) < num_vertices:
            current_vertex = min((v for v in range(1, num_vertices + 1) if v not in visited), key=lambda x: dist[x - 1])
            visited.add(current_vertex)

            for neighbor in range(1, num_vertices + 1):
                if self.WEIGHT_MATRIX[current_vertex - 1][neighbor - 1] != 0:
                    if dist[current_vertex - 1] + self.WEIGHT_MATRIX[current_vertex - 1][neighbor - 1] < dist[neighbor - 1]:
                        dist[neighbor - 1] = dist[current_vertex - 1] + self.WEIGHT_MATRIX[current_vertex - 1][neighbor - 1]
                        paths[neighbor - 1] = paths[current_vertex - 1] + [current_vertex]

        return dist, paths



    
    def __min_distance_vertex(self, dist, visited):
        min_dist = float('inf')
        min_vertex = -1
        for v in range(len(dist)):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_vertex = v
        return min_vertex

    def compute_distance_matrix(self):
        num_vertices = len(self.WEIGHT_MATRIX)
        distance_matrix = np.zeros((num_vertices, num_vertices), dtype=int)

        for i in range(num_vertices):
            shortest_distances = self.dijkstra_shortest_path(i)
            distance_matrix[i] = shortest_distances

        self.distance_matrix = distance_matrix
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

    def get_graph_for_networkx(self):
        G = nx.Graph()
        num_vertices = len(self.WEIGHT_MATRIX)
        for i in range(num_vertices):
            for j in range(i+1, num_vertices):
                if self.WEIGHT_MATRIX[i][j] != 0:
                    G.add_edge(i+1, j+1, weight=self.WEIGHT_MATRIX[i][j])
        return G
    
    def kruskal_minimum_spanning_tree(self):
        if self.graph_representation != GraphRepresentation.NEIGHBOURHOOD_MATRIX:
            raise ValueError("Minimum spanning tree computation requires the graph to be represented as a neighbourhood matrix.")
        
        num_vertices = len(self.WEIGHT_MATRIX)
        mst = nx.Graph()

        # Initialize the disjoint-set data structure
        sets = [{i} for i in range(num_vertices)]

        # Initialize the edges list
        edges = []

        # Create a list of edges with weights
        for i in range(num_vertices):
            for j in range(i+1, num_vertices):
                if self.WEIGHT_MATRIX[i][j] != 0:
                    edges.append((i, j, self.WEIGHT_MATRIX[i][j]))

        # Sort the edges by weight
        edges.sort(key=lambda x: x[2])
        print(edges)
        # Kruskal's algorithm
        for edge in edges:
            u, v, weight = edge

            # Find the sets containing u and v
            u_set = None
            v_set = None
            for s in sets:
                if u in s:
                    u_set = s
                if v in s:
                    v_set = s

            # If u and v belong to different sets, add the edge to the MST
            if u_set != v_set:
                mst.add_edge(u+1, v+1, weight=weight)
              
                # Union operation: merge the sets containing u and v
                u_set.update(v_set)
                sets.remove(v_set)

        return mst
    
    def prim_minimum_spanning_tree(self):
        if self.graph_representation != GraphRepresentation.NEIGHBOURHOOD_MATRIX:
            raise ValueError("Minimum spanning tree computation requires the graph to be represented as a neighbourhood matrix.")
        
        num_vertices = len(self.array)
        mst = nx.Graph()
        visited = [False] * num_vertices
        key = [float('inf')] * num_vertices
        parent = [-1] * num_vertices

        key[0] = 0  # Klucz dla pierwszego wierzchołka

        for _ in range(num_vertices):
            # Znajdź wierzchołek o najmniejszym kluczu, który jeszcze nie został odwiedzony
            min_key = float('inf')
            min_index = -1
            for v in range(num_vertices):
                if not visited[v] and key[v] < min_key:
                    min_key = key[v]
                    min_index = v
            
            visited[min_index] = True

            # Dodaj krawędzie do MST
            if parent[min_index] != -1:
                mst.add_edge(min_index + 1, parent[min_index] + 1, weight=key[min_index])
            # Wizualizacja minimalnego drzewa rozpinającego

            # Zaktualizuj klucze dla sąsiednich wierzchołków
            for v in range(num_vertices):
                if self.array[min_index][v] and not visited[v] and self.array[min_index][v] < key[v]:
                    parent[v] = min_index
                    key[v] = self.array[min_index][v]

        return mst