import heapq

def bellman_ford(G, weights, source):
    distance = {vertex: float('inf') for vertex in G.nodes}
    distance[source] = 0
    
    for _ in range(len(G) - 1):
        for u, v in weights:
            if distance[u] + weights[u, v] < distance[v]:
                distance[v] = distance[u] + weights[u, v]
    
    for u, v in weights:
        if distance[u] + weights[u, v] < distance[v]:
            raise ValueError("Graph contains a negative weight cycle")
    
    return distance

def dijkstra(G, weights, source):
    distance = {vertex: float('inf') for vertex in G}
    distance[source] = 0
    priority_queue = [(0, source)]
    
    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)
        
        if current_distance > distance[u]:
            continue
        
        for v in G[u]:
            weight = weights[(u, v)]
            distance_through_u = current_distance + weight
            if distance_through_u < distance[v]:
                distance[v] = distance_through_u
                heapq.heappush(priority_queue, (distance[v], v))
    
    return distance

def johnson(G, weights):
    new_node = len(G.nodes) 
    G.add_node(new_node)
    for node in G.nodes:
        if node != new_node:
            weights[(new_node, node)] = 0
            G.add_edge(new_node, node)
    
    try:
        h = bellman_ford(G, weights, new_node)
    except ValueError as e:
        print(e)
        return None
    
    G.remove_node(new_node)
    for u, v in list(weights.keys()):
        if u == new_node or v == new_node:
            del weights[(u, v)]
    
    new_weights = {}
    for u, v in weights:
        new_weights[(u, v)] = weights[(u, v)] + h[u] - h[v]
    
    distances = {}
    for u in G.nodes:
        distances[u] = dijkstra(G, new_weights, u)
        for v in G.nodes:
            if distances[u][v] != float('inf'):
                distances[u][v] += h[v] - h[u]
    
    return distances