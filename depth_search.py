from width_search import *
import os

def depth_search(graph, n):
    answer = ''
    while answer not in ('find', 'search'):
        answer = input("Ktora operacje wybierasz: \n-search\n-find\n")
    os.system('cls')
    if answer == 'find':
        return find(graph, n)
    elif answer == 'search':
        visited = [False] * n
        result = []

        def dfs(vertex):
            visited[vertex] = True
            result.append(vertex)
            for i in range(n):
                if graph[vertex][i] == 1 and not visited[i]:
                    dfs(i)

        for start in range(n):
            if not visited[start]:
                dfs(start)
        for i in range(len(result)):
            result[i] += 1
        return result
    else:
        print("Niepoprawna operacja. Wybierz 'search' lub 'find'.")
        return 
