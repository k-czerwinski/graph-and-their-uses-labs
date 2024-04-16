import numpy as np
from DirectedGraph import DirectedGraphFromAdjacencyList

class PageRank:
    def __init__(self, graph, damping_factor=0.85, epsilon=1.0e-8, max_iter=100):
        self.graph = graph
        self.damping_factor = damping_factor
        self.epsilon = epsilon
        self.max_iter = max_iter
        self.num_nodes = len(graph.nodes())
        self.transition_matrix = self.create_transition_matrix()
        self.page_rank = self.calculate_page_rank()

    def create_transition_matrix(self):
        transition_matrix = np.zeros((self.num_nodes, self.num_nodes))
        for i, node in enumerate(self.graph.nodes()):
            neighbors = list(self.graph.neighbors(node))
            if neighbors:
                for neighbor in neighbors:
                    transition_matrix[i][list(self.graph.nodes()).index(neighbor)] = 1 / len(neighbors)
            else:
                transition_matrix[i] = np.ones(self.num_nodes) / self.num_nodes
        return transition_matrix.T

    def calculate_page_rank(self):
        page_rank = np.ones(self.num_nodes) / self.num_nodes
        for _ in range(self.max_iter):
            new_page_rank = self.damping_factor * np.dot(self.transition_matrix, page_rank) + (1 - self.damping_factor) / self.num_nodes
            if np.linalg.norm(new_page_rank - page_rank, ord=1) < self.epsilon:
                return new_page_rank
            page_rank = new_page_rank
        return page_rank

    def print_pagerank(self):
        sorted_pagerank = sorted(enumerate(self.page_rank), key=lambda x: x[1], reverse=True)
        for idx, rank in sorted_pagerank:
            print("{} ==> PageRank = {:.6f}".format(chr(idx+65), rank))

# Example usage
filename = "adjacency_list.txt"
G = DirectedGraphFromAdjacencyList(filename).graph
pagerank = PageRank(G)
print("PageRank values:")
pagerank.print_pagerank()
