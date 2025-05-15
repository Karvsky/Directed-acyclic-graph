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
        width = len(str(n)) + 1
        print('   | ', end='')
        for i in range(n):
            print(f'{i + 1:>{width}}', end=' ')
        print()
        print('---+', end='')
        for i in range(n):
            print('-' * width, end='')
        print()
        for i in range(n):
            print(f'{i + 1:<{width}}| ', end='')
            for j in range(n):
                print(f'{graph[i][j]:>{width}}', end=' ')
            print()


    elif (answer == 'list'):
        print()
    else:
        print(graph)