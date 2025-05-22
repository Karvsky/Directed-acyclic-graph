def kahn(graph, n, rep):
    """Kahn's algorithm for topological sorting using rep: 'matrix','list','table'. Returns 1-based order."""
    # construct adjacency list 0-based and compute in-degrees
    in_degree = [0] * n
    adj = [[] for _ in range(n)]
    if rep == 'matrix':
        for u in range(n):
            for v in range(n):
                if graph[u][v] == 1:
                    adj[u].append(v)
                    in_degree[v] += 1
    elif rep == 'list':
        for u, neighbors in enumerate(graph):
            for v in neighbors:
                adj[u].append(v-1)
                in_degree[v-1] += 1
    else:  # table
        for u, v in graph:
            adj[u-1].append(v-1)
            in_degree[v-1] += 1
    # initialize zero in-degree queue
    S = [i for i in range(n) if in_degree[i] == 0]
    L = []
    while S:
        u = S.pop(0)
        L.append(u+1)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                S.append(v)
    if len(L) != n:
        raise ValueError("Graf zawiera cykl - sortowanie topologiczne niemożliwe")
    return L