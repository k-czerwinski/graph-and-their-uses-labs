from lab1.graph_representation.SimpleGraph import *
from graph_drawing.utils import *
from random_graph.utils import *

# ex 1
file_path = "sample_data/adjacency_list.txt"
adjacency_list = SimpleGraph.load_adjacency_list(file_path)
graph = SimpleGraph(adjacency_list, GraphRepresentation.NEIGHBOURHOOD_LIST) # can be adjusted to our needs

np.savetxt('./target/ex3_adjacency_matrix.txt', graph.get_adjacency_matrix(), fmt='%i')
np.savetxt('./target/ex3_incidence_matrix.txt', graph.get_incidence_matrix(), fmt='%i')

# ex 2
file_path = "sample_data/adjacency_list.txt"
adjacency_list = SimpleGraph.load_adjacency_list(file_path)
graph = SimpleGraph(adjacency_list, GraphRepresentation.NEIGHBOURHOOD_LIST)

draw_graph_on_circle_from_adjacency_matrix(graph.get_adjacency_matrix(), './target/ex2_graph.png')

# ex 3
G1 = generate_random_graph_with_edge_probability(10,0.7)
draw_graph_on_circle_from_adjacency_matrix(G1, './target/ex3_random_graph_edge_probabilities.png')

G2 = generate_random_graph(10,45)
draw_graph_on_circle_from_adjacency_matrix(G2, './target/ex3_random_graph_number_of_edges.png')