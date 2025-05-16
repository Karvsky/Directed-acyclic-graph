from width_search import *
import os

def depth_search(graph, n):
    answer = ''
    os.system('cls' if os.name=='nt' else 'clear')

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

