import os

def Print(graph, n):
    os.system('cls' if os.name=='nt' else 'clear')
    print("Macierz sąsiedztwa:")
    col_width = max(len(str(n)), len(str(-1))) + 1
    print(' ' * (col_width + 2) + '|', end='')
    for j in range(n): print(f' {j+1:^{col_width}} |', end='')
    print()
    print('-' * (col_width + 2) + '+', end='')
    for _ in range(n): print('-' * (col_width + 2) + '+', end='')
    print()
    for i in range(n):
        print(f' {i+1:^{col_width}} |', end='')
        for j in range(n): print(f' {graph[i][j]:^{col_width}} |', end='')
        print()
    print("\nLista sąsiedztwa:")
    for u in range(n):
        neighbors = [str(v+1) for v in range(n) if graph[u][v] == 1]
        print(f"{u+1} -> {' -> '.join(neighbors)}")
    print("\nTabela krawędzi:")
    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1:
                print(f"{u+1} -> {v+1}")
