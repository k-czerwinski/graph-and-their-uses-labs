import networkx as nx
import sys

def bellman_ford(G, weights, source):
    # Step 1: Initialize distances and predecessors
    distances = {node: sys.maxsize for node in G.nodes}
    distances[source] = 0
    predecessors = {node: None for node in G.nodes}

    # Step 2: Relax edges repeatedly
    for _ in range(len(G.nodes) - 1):
        for u, v in G.edges:
            if distances[u] + weights[u][v] < distances[v]:
                distances[v] = distances[u] + weights[u][v]
                predecessors[v] = u

    # Step 3: Check for negative cycles
    for u, v in G.edges:
        if distances[u] + weights[u][v] < distances[v]:
            raise ValueError("Graph contains a negative cycle")

    return distances, predecessors

