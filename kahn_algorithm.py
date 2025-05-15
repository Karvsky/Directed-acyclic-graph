def kahn(graph, n):

    in_degree = [0] * n
    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1:
                in_degree[v] += 1

    queue = [i for i in range(n) if in_degree[i] == 0]
    order = []

    while queue:
        u = queue.pop(0)
        order.append(u + 1)
        for v in range(n):
            if graph[u][v] == 1:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

    if len(order) != n:
        print("Graf zawiera cykl - sortowanie topologiczne niemożliwe")
        return
    return order