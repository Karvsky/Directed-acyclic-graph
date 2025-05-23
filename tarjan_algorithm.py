def Tarjan(graph, n, rep):
    def get_neighbors(u):
        if rep == 'matrix':
            return [v for v in range(n) if graph[u][v] == 1]
        elif rep == 'list':
            return [v-1 for v in graph[u]]
        else:
            return [dst-1 for (src, dst) in graph if src-1 == u]
    status = [0] * n
    result = []
    def dfs(u):
        if status[u] == 1:
            raise ValueError("Graf zawiera cykl - sortowanie topologiczne niemożliwe")
        if status[u] == 2:
            return
        status[u] = 1
        for v in get_neighbors(u):
            if status[v] != 2:
                dfs(v)
        status[u] = 2
        result.append(u+1)
    for u in range(n):
        if status[u] == 0:
            dfs(u)
    return result[::-1]

