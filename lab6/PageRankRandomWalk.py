import networkx as nx
import numpy as np
from DirectedGraph import DirectedGraphFromAdjacencyList

class PageRankRandomWalkTeleportation:
    def __init__(self, graph, num_steps, damping_factor=0.85):
        self.graph = graph
        self.num_nodes = len(graph.nodes())
        self.num_steps = num_steps
        self.damping_factor = damping_factor
        self.page_rank = self.calculate_page_rank()

    def calculate_page_rank(self):
        # Inicjalizacja licznika odwiedzin dla każdego wierzchołka
        visit_counts = {node: 0 for node in self.graph.nodes()}
        
        # Wybierz losowy wierzchołek startowy
        current_node = np.random.choice(list(self.graph.nodes()))

        for _ in range(self.num_steps):
            # Błądzenie przypadkowe z prawdopodobieństwem (1 - d)
            if np.random.rand() > self.damping_factor or not list(self.graph.neighbors(current_node)):
                current_node = np.random.choice(list(self.graph.nodes()))
            else:
                current_node = np.random.choice(list(self.graph.neighbors(current_node)))

            # Zlicz odwiedziny danego wierzchołka
            visit_counts[current_node] += 1

        # Normalizacja wyników PageRank przez liczbę kroków
        page_rank = {node: count / self.num_steps for node, count in visit_counts.items()}
        return page_rank

# Example usage
filename = "adjacency_list.txt"
G = DirectedGraphFromAdjacencyList(filename).graph

num_steps = 10000  # Liczba kroków
pagerank_rw_teleport = PageRankRandomWalkTeleportation(G, num_steps)

# Sortowanie wyników PageRank
sorted_pagerank = sorted(pagerank_rw_teleport.page_rank.items(), key=lambda x: x[1], reverse=True)

# Wydruk posortowanych wyników

for idx, (node, rank) in enumerate(sorted_pagerank, 1):
    print("{} ==> PageRank = {:.6f}".format(node, rank))