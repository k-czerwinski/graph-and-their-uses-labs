import numpy as np
import SimpleGraph as sg

def load_adjacency_list(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            row_data = [int(x) for x in line.split()]
            data.append(row_data)
    return data

file_path = "sample_data/adjacency_list.txt"
data = load_adjacency_list(file_path)
neighborhood_list = np.array(data, dtype=object)
graph = sg.SimpleGraph(neighborhood_list, sg.GraphRepresentation.NEIGHBOURHOOD_LIST)

np.savetxt('target/adjacency_matrix.txt', graph.get_adjacency_matrix(), fmt='%i')
np.savetxt('target/incidence_matrix.txt', graph.get_incidence_matrix(), fmt='%i')