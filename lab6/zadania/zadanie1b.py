from utils import PageRank, DirectedGraphFromAdjacencyList

# Example usage
filename = "adjacency_list.txt"
G = DirectedGraphFromAdjacencyList(filename).graph
pagerank = PageRank(G)
print("PageRank values:")
pagerank.print_pagerank()
