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
    exists = False
    if rep == 'matrix':
        exists = (graph[a-1][b-1] == 1)
    elif rep == 'list':
        exists = (b in graph[a-1])
    elif rep == 'table':
        exists = ((a, b) in graph)
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


