def Tarjan(graph, n):
    oznaczony = ['nieoznaczony']*n
    L = []
    print(f"Rozpoczynamy algorytm Tarjana dla grafu o {n} wierzchołkach.")
    for i in range(n):
        if oznaczony[i] == 'nieoznaczony':
            print(f"Odwiedzamy wierzchołek {i}")
            visit(i, oznaczony, graph, L) 
    if L:
        return L[::-1]
    else:
        print("Graf jest acykliczny, ale brak porządku topologicznego.")
def visit(n, oznaczony, graph, L):
    if oznaczony[n] == 'staly':
        return
    elif oznaczony[n] == 'tymczasowy':
        print("graf ma cykl")
        return
    oznaczony[n] = 'tymczasowy'
    for i in range(n):
        if graph[n][i] == 1:
            visit(i, oznaczony, graph, L)
    oznaczony[n] = 'staly'
    L.append(n)

