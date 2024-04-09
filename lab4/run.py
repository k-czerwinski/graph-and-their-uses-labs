from digraph_drawing.utils import draw_digraph_from_adjacency_matrix, draw_graph_with_weights
from korsaju.utils import korsaju
from random_digraph.utils import generate_random_digraph_with_edge_probability, generate_random_weights
from collections import defaultdict
import networkx as nx
# from bellman_ford.utils import bellman_ford

# ex 1
print('---EXERCISE 1---')
number_of_vertices = int(input("Enter the number of vertices: "))
edge_exist_probability = float(input("Enter the probability of edge existing: "))
adjency_matrix = generate_random_digraph_with_edge_probability(number_of_vertices, edge_exist_probability)
print(adjency_matrix)
draw_digraph_from_adjacency_matrix(adjency_matrix, 'ex1_graph.png')
print('---EXERCISE 2---')
# ex 2
components = korsaju(adjency_matrix)
group_vertices = defaultdict(list)
for vertex, group in enumerate(components):
    group_vertices[group].append(vertex + 1)

print("Strongly Connected Component Groups:")
for group, vertices in group_vertices.items():
    print("Group {}: {}".format(group, vertices))
    
#ex 3
print('---EXERCISE 3---')
if(len(group_vertices) == 1):
    print("The graph is strongly connected")
    G, weights = generate_random_weights(adjency_matrix)
    draw_graph_with_weights(G, weights, 'ex3_graph.png')
else:
    print("The graph is not strongly connected")