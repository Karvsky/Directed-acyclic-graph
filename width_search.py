import random, os

def find(graph, n, rep):
    a = b = -1
    while True:
        try:
            a = int(input("Podaj pierwszy wierzcholek (source): "))
            b = int(input("Podaj drugi wierzcholek (target): "))
            if a < 1 or a > n or b < 1 or b > n:
                print("Podaj ponownie wierzcholki (poza zakresem)")
                continue
            break
        except ValueError:
            print("Niepoprawna wartosc, podaj liczbe calkowita")
    def get_neighbors(u):
        if rep == 'matrix':
            return [v for v in range(n) if graph[u][v] == 1]
        elif rep == 'list':
            return [v-1 for v in graph[u]]
        else:
            return [dst-1 for (src, dst) in graph if src-1 == u]
    exists = (b-1) in get_neighbors(a-1)
    if exists:
        print(f"True: krawedz ({a},{b}) istnieje w grafie!")
    else:
        print(f"False: krawedz ({a},{b}) nie istnieje w grafie!")
    return exists

def width(graph, n):
    answer = ''
    os.system('cls' if os.name=='nt' else 'clear')

    visited = [False] * n
    result = []
    for start_vertex in range(n):
        if visited[start_vertex]:
            continue
        queue = [start_vertex]
        visited[start_vertex] = True
        while queue:
            current = queue.pop(0)
            result.append(current)
            for i in range(n):
                if graph[current][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
    for i in range(len(result)):
        result[i] += 1
    return result


