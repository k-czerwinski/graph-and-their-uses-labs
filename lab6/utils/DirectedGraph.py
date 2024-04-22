import networkx as nx
import matplotlib.pyplot as plt

class DirectedGraphFromAdjacencyList:
    def __init__(self, filename):
        self.adjacency_list = self.read_adjacency_list(filename)
        self.graph = self.create_directed_graph()

    def read_adjacency_list(self, filename):
        adjacency_list = {}
        with open(filename, 'r') as file:
            for line in file:
                node, neighbors = line.strip().split(' : ')
                adjacency_list[node] = neighbors.split(',')
        
        return adjacency_list

    def create_directed_graph(self):
        G = nx.DiGraph()
        for node in self.adjacency_list.keys():
            G.add_node(node)
        for node, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
        return G

    def draw_graph(self):
        pos = nx.circular_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=1000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
        plt.title("Directed Graph")
        plt.show()

# # Usage example
# filename = "adjacency_list.txt"  # Provide the filename here
# graph_creator = DirectedGraphFromAdjacencyList(filename)
# graph_creator.draw_graph()