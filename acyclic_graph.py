import random, os


def generate(nodes, saturation):
    max_edges = nodes * (nodes - 1) // 2
    edge_count = int(max_edges * (saturation / 100))
    adjacency_matrix = [[0] * nodes for i in range(nodes)]

    for i in range(nodes - 1):
        adjacency_matrix[i][i + 1] = 1
        adjacency_matrix[i + 1][i] = -1

    edges_added = nodes - 1

    while edges_added < edge_count:
        i, j = random.sample(range(nodes), 2)
        if i < j and adjacency_matrix[i][j] == 0:
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = -1
            edges_added += 1
    os.system('cls')
    return adjacency_matrix


