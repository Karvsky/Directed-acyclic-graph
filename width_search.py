import random

def width(graph, n):
    pom1 = 0
    answer = input("Ktora operacje wybierasz: \n-search\n-find\n")
    if (answer == 'find'):
        answer = 'find'
        a = int(input("Podaj pierwszy wierzcholek z ktorego ma wychodzic krawedz: "))
        b = int(input("Podaj drugi wierzcholek: "))
    elif (answer == 'search'):
        answer = 'search'
    visited = [False]*n
    queue = []
    #start = random.randint(0, n - 1)
    start = 0
    visited[start] = True
    queue.append(start)
    while (queue != []):
       current = queue.pop(0)
       print(current)
       for i in range(n):
           if (graph[current][i] == 1 and visited[i] == False):
               if (answer =='find' and current == a and i == b):
                   pom1 = 1
               visited[i] = True
               queue.append(i)
    if answer == 'find':
        if pom1 == 1:
            print("Edge", a, "and", b, "exist")
        elif pom1 == 0:
            print("Edge", a, "and", b, "not exist")
    elif answer == 'search':
        return visited
