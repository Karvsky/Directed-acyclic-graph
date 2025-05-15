def Tarjan(adj_matrix, n):
    status = [0] * n
    L = []
    
    def visit(node):
        if status[node] == 2:
            return
        if status[node] == 1:
            raise ValueError("Graf zawiera cykl - sortowanie topologiczne niemożliwe")
        
        status[node] = 1
        
        for next_node in range(n):
            if adj_matrix[node][next_node] == 1:
                visit(next_node)
        
        status[node] = 2
        L.append(node)
    
    for node in range(n):
        if status[node] == 0:
            visit(node)
    
    print (L[::-1])

