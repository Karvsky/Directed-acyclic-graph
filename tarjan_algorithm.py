def Tarjan(graph, n, rep):
    """Topological sort via DFS using user-selected representation rep: 'matrix','list','table'."""
    # build adjacency list 0-based
    if rep == 'matrix':
        adj_list = [[v for v in range(n) if graph[u][v] == 1] for u in range(n)]
    elif rep == 'list':
        # graph: list of neighbor lists, 1-based values
        adj_list = [[v-1 for v in neighbors] for neighbors in graph]
    else:  # table
        adj_list = [[] for _ in range(n)]
        for u,v in graph:
            adj_list[u-1].append(v-1)
    status = [0] * n
    result = []
    def dfs(u):
        if status[u] == 1:
            raise ValueError("Graf zawiera cykl - sortowanie topologiczne niemożliwe")
        if status[u] == 2:
            return
        status[u] = 1
        for v in adj_list[u]:
            if status[v] != 2:
                dfs(v)
        status[u] = 2
        result.append(u+1)
    for u in range(n):
        if status[u] == 0:
            dfs(u)
    return result[::-1]

