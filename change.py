import os

def Print(graph, n):
    answer = ''
    pom1 = 0
    while (answer != 'matrix' and answer != 'list' and answer != 'table'):
        if pom1 == 0:
            answer = input("Wpisz jedno z wybranych:\n-matrix\n-list\n-table\n")
        else:
            print("Podales niedopuszczalna odpowiedz. Wpisz jeszcze raz: ")
            answer = input()
        pom1 += 1
    if answer == 'matrix':
        os.system('cls')
        col_width = max(len(str(n)), len(str(-1))) + 1
        print(' ' * (col_width + 2) + '|', end='')
        for j in range(n):
            print(f' {j + 1:^{col_width}} |', end='')
        print()
        print('-' * (col_width + 2) + '+', end='')
        for j in range(n):
            print('-' * (col_width + 2) + '+', end='')
        print()
        for i in range(n):
            print(f' {i + 1:^{col_width}} |', end='')
            for j in range(n):
                print(f' {graph[i][j]:^{col_width}} |', end='')
            print()
    elif (answer == 'list'):
        os.system('cls')
        for i in range(n):
            print(i+1, end="")
            for j in range(n):
                if graph[i][j] != 1: continue
                print("->", end="")
                print(f'{j + 1}', end="")
            print("\n")
    else:
        os.system('cls')
        print(graph)