def kahn(graph, n):
    in_degree = [sum(1 for u in range(n) if graph[u][v] == 1) for v in range(n)]

    S = [i for i in range(n) if in_degree[i] == 0]
    L = []

    while S:
        u = S.pop(0)
        L.append(u + 1)
        for m in range(n):
            if graph[u][m] == 1:
                graph[u][m] = 0
                in_degree[m] -= 1
                if in_degree[m] == 0:
                    S.append(m)

    if any(in_degree[v] > 0 for v in range(n)):
        print("Graf zawiera cykl - sortowanie topologiczne niemożliwe")
        return
    return L