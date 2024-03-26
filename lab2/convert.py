from graph_representation.SimpleGraph import  *

file_path = "sample_data/adjacency_list.txt"
adjacency_list = SimpleGraph.load_adjacency_list(file_path)
graph = SimpleGraph(adjacency_list, GraphRepresentation.NEIGHBOURHOOD_LIST)

np.savetxt('../target/adjacency_matrix.txt', graph.get_adjacency_matrix(), fmt='%i')
np.savetxt('../target/incidence_matrix.txt', graph.get_incidence_matrix(), fmt='%i')