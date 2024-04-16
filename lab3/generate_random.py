from graph_drawing.utils import *
from random_graph.utils import *

G = generate_random_graph_with_edge_probability(10,0.7)
draw_graph_on_circle_from_adjacency_matrix(G, './target/random_graph.png')
