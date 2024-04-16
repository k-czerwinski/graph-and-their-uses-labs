import networkx as nx

def components_R(nr, v, G, comp):
    for neighbor in G.neighbors(v):
        if comp[neighbor] == -1:
            comp[neighbor] = nr
            components_R(nr, neighbor, G, comp)

def components(G):
    comp = {v: -1 for v in G.nodes()}
    nr = 0
    for v in G.nodes():
        if comp[v] == -1:
            nr += 1
            comp[v] = nr
            components_R(nr, v, G, comp)
    return comp

def nodes_in_component(G, comp, c):
    return [v for v in G.nodes() if comp[v] == c]

def largest_connected_component(G):
    comp = components(G)
    most_common_value = max(set(comp.values()), key = list(comp.values()).count)
    return nodes_in_component(G, comp, most_common_value)

def color_map(comp):
    return [comp[v] for v in comp]