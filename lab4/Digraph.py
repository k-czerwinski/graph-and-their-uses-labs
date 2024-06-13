import numpy as np
from enum import Enum


class GraphRepresentation(Enum):
    NEIGHBOURHOOD_LIST = 1,
    NEIGHBOURHOOD_MATRIX = 2,
    INCIDENCE_MATRIX = 3


class Digraph:
    def __init__(self, input_array, graph_representation):
        if not isinstance(input_array, np.ndarray):
            raise TypeError("Input must be a NumPy array")
        if not isinstance(graph_representation, GraphRepresentation):
            raise TypeError("Array representation must be a member of ArrayRepresentation Enum")
        self.array = input_array
        self.graph_representation = graph_representation

    def get_graph_representation(self):
        return self.graph_representation

    def get_adjacency_list(self):
        if self.graph_representation is GraphRepresentation.NEIGHBOURHOOD_LIST:
            return self.array
        elif self.graph_representation is GraphRepresentation.NEIGHBOURHOOD_MATRIX:
            return self.__adjacency_matrix_to_adjacency_list(self.array)
        elif self.graph_representation is GraphRepresentation.INCIDENCE_MATRIX:
            return self.__incidence_matrix_to_adjacency_list(self.array)

    def get_incidence_matrix(self):
        if self.graph_representation is GraphRepresentation.INCIDENCE_MATRIX:
            return self.array
        elif self.graph_representation is GraphRepresentation.NEIGHBOURHOOD_LIST:
            return self.__adjacency_list_to_incidence_matrix(self.array)
        elif self.graph_representation is GraphRepresentation.NEIGHBOURHOOD_MATRIX:
            adjacency_list = self.__adjacency_matrix_to_adjacency_list(self.array)
            return self.__adjacency_list_to_incidence_matrix(adjacency_list)

    def get_adjacency_matrix(self):
        if self.graph_representation is GraphRepresentation.NEIGHBOURHOOD_MATRIX:
            return self.array
        elif self.graph_representation is GraphRepresentation.NEIGHBOURHOOD_LIST:
            return self.__adjacency_list_to_adjacency_matrix(self.array)
        elif self.graph_representation is GraphRepresentation.INCIDENCE_MATRIX:
            adjacency_list = self.__incidence_matrix_to_adjacency_list(self.array)
            return self.__adjacency_list_to_adjacency_matrix(adjacency_list)

    @staticmethod
    def __adjacency_list_to_adjacency_matrix(neighbors_list):
        n = neighbors_list.size
        matrix = np.zeros((n, n), dtype=int)
        for list in neighbors_list:
            i = list[0] - 1
            for x in list[1:]:
                matrix[i][x - 1] = 1
        return matrix

    @staticmethod
    def __adjacency_list_to_incidence_matrix(adjacency_list):
        n = len(adjacency_list)
        edges = []
        for i in range(n):
            v_idx = adjacency_list[i][0] - 1
            for v in adjacency_list[i][1:]:
                edges.append((v_idx, v - 1))

        m = len(edges)
        incidence_matrix = np.zeros((n, m), dtype=int)

        for edge_index, (start, end) in enumerate(edges):
            incidence_matrix[start][edge_index] = -1
            incidence_matrix[end][edge_index] = 1

        return incidence_matrix

    @staticmethod
    def __incidence_matrix_to_adjacency_list(incidence_matrix):
        n, m = incidence_matrix.shape
        adjacency_list = [[] for _ in range(n)]
        for i in range(n):
            adjacency_list[i].append(i + 1)

        for j in range(m):
            start, end = np.where(incidence_matrix[:, j] == -1)[0][0], np.where(incidence_matrix[:, j] == 1)[0][0]
            adjacency_list[start].append(end + 1)

        return adjacency_list

    @staticmethod
    def __adjacency_matrix_to_adjacency_list(adjacency_matrix):
        n = adjacency_matrix.shape[0]
        adjacency_list = [[] for _ in range(n)]
        for i in range(n):
            adjacency_list[i].append(i + 1)  # Include the vertex itself at the start of the list
            for j in range(n):
                if adjacency_matrix[i][j] == 1:
                    adjacency_list[i].append(j + 1)
        return adjacency_list

    @staticmethod
    def load_adjacency_list(file_path):
        data = []
        with open(file_path, 'r') as file:
            for line in file:
                row_data = [int(x) for x in line.split()]
                data.append(row_data)

        neighborhood_list = np.array(data, dtype=object)
        return neighborhood_list

