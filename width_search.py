import random, os

def find(graph, n):
    a = -2
    b = -2
    while (a - 1 < 0 or a - 1 > n) or (b - 1 < 0 or b - 1 > n):
        try:
            a = int(input("Podaj pierwszy wierzcholek z ktorego ma wychodzic krawedz: "))
            b = int(input("Podaj drugi wierzcholek: "))
            if (a < 0 or a + 1 > n) or (b < 0 or b + 1 > n):
                print("Podaj ponownie wierzcholki")
        except ValueError:
            a = -2
            b = -2
            print("Niepoprawna wartosc, podaj liczbe calkowita")
    if graph[a - 1][b - 1] == 1:
        print(f"True: edge ({a},{b}) exists in the Graph!")
        return True
    else:
        print(f"False: edge ({a},{b}) does not exist in the Graph!")
        return False

def width(graph, n):
    answer = ''
    while (answer != 'find' and answer != 'search'):
        answer = input("Ktora operacje wybierasz: \n-search\n-find\n")
    os.system('cls')
    if answer == 'find':
        find(graph, n)

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

        for i in range(len(result)):
            result[i] += 1
        return result

    else:
        print("Niepoprawna operacja. Wybierz 'search' lub 'find'.")
        return 

    
