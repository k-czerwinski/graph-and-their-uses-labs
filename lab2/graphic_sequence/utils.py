import networkx as nx
import random

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


def can_swap(G, edge1, edge2):
    a, b = edge1
    c, d = edge2
    if a == c or a == d or b == c or b == d:
        return False  # Zapobiega pętlom
    if G.has_edge(a, d) or G.has_edge(b, c):
        return False  # Zapobiega wielokrotnym krawędziom
    return True
def swap_edges(G):
    edges = list(G.edges())
    random.shuffle(edges)
    for i in range(len(edges)):
        for j in range(i + 1, len(edges)):
            if can_swap(G, edges[i], edges[j]):
                # Dokonuje zamiany krawędzi
                a, b = edges[i]
                c, d = edges[j]
                G.remove_edge(a, b)
                G.remove_edge(c, d)
                G.add_edge(a, d)
                G.add_edge(b, c)
                return True
    return False

def randomize_graph(G, iterations=1):
    for _ in range(iterations):
        swap_edges(G)
    return G