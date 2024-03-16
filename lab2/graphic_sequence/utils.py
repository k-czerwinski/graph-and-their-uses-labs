import networkx as nx

def is_graphic_sequence(sequence):
    sequence = sorted(sequence, reverse=True)
    while sequence:
        if sequence[0] < 0:
            return False
        if sequence[0] == 0:
            sequence = sequence[1:]
            continue
        for i in range(1, sequence[0] + 1):
            sequence[i] -= 1
        sequence = sorted(sequence[1:], reverse=True)
    return True


def construct_graph_from_sequence(sequence):
    if not is_graphic_sequence(sequence):
        return None

    G = nx.Graph()

    vertices_and_degrees = [(i, deg) for i, deg in enumerate(sequence)]

    while True:
        vertices_and_degrees.sort(key=lambda x: x[1], reverse=True)

        if vertices_and_degrees[0][1] == 0:
            return G

        max_degree = vertices_and_degrees[0][1]

        for i in range(1, max_degree + 1):
            G.add_edge(vertices_and_degrees[0][0], vertices_and_degrees[i][0])
            vertices_and_degrees[i] = (vertices_and_degrees[i][0], vertices_and_degrees[i][1] - 1)

        vertices_and_degrees = vertices_and_degrees[1:]

        if len(vertices_and_degrees) < max_degree:
            return None

    return G
