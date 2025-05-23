def kahn(graph, n, rep):
    def get_neighbors(u):
        if rep == 'matrix':
            return [v for v in range(n) if graph[u][v] == 1]
        elif rep == 'list':
            return [v-1 for v in graph[u]]
        else:
            return [dst-1 for (src, dst) in graph if src-1 == u]
    in_degree = [0] * n
    for u in range(n):
        for v in get_neighbors(u):
            in_degree[v] += 1
    S = [i for i in range(n) if in_degree[i] == 0]
    L = []
    while S:
        u = S.pop(0)
        L.append(u+1)
        for v in get_neighbors(u):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                S.append(v)
    if len(L) != n:
        raise ValueError("Graf zawiera cykl - sortowanie topologiczne niemożliwe")
    return L
