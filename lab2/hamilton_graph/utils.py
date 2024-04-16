import networkx as nx

def is_hamiltonian(graph: nx.Graph):
    def dfs(graph, current_node, visited, path):
        visited[current_node] = True
        path.append(current_node)

        if len(path) == len(graph.nodes()):
            if graph.has_edge(path[0], path[-1]):
                return True, path
            else:
                if path:
                    path.pop()
                visited[current_node] = False
                return False, []

        for neighbor in graph.neighbors(current_node):
            if not visited[neighbor]:
                result, path = dfs(graph, neighbor, visited, path)
                if result:
                    return True, path

        if path:
            path.pop()
        visited[current_node] = False
        return False, []

    visited = {node: False for node in graph.nodes()}
    path = []

    for node in graph.nodes():
        result, path = dfs(graph, node, visited, path)
        if result:
            return True, path

    return False, []