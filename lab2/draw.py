from graph_representation.SimpleGraph import *
from graph_drawing.utils import *

file_path = "sample_data/adjacency_list.txt"
adjacency_list = SimpleGraph.load_adjacency_list(file_path)
graph = SimpleGraph(adjacency_list, GraphRepresentation.NEIGHBOURHOOD_LIST)

draw_graph_on_circle_from_adjacency_matrix(graph.get_adjacency_matrix(), '../target/graph.png')