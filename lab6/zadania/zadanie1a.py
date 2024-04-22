from utils import PageRankRandomWalkTeleportation, DirectedGraphFromAdjacencyList


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