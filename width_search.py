import random

def width(graph, n):
    print(graph)
    print(n)
    answer = input("Ktora operacje wybierasz: \n-search\n-find\n")

    if answer == 'find':
        a = int(input("Podaj pierwszy wierzcholek z ktorego ma wychodzic krawedz: "))
        b = int(input("Podaj drugi wierzcholek: "))
        if 0 <= a < n and 0 <= b < n and graph[a][b] == 1:
            print(f"True: edge ({a},{b}) exists in the Graph!")
        else:
            print(f"False: edge ({a},{b}) does not exist in the Graph!")
        return

    elif answer == 'search':
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

        print("inline:", " ".join(map(str, result)))
        return result

    else:
        print("Niepoprawna operacja. Wybierz 'search' lub 'find'.")
        return None

    
