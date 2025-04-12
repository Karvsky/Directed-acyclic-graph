def generator(n):
    pom1 = []
    for i in range(n):
        pom1.append([0]*n)
    for i in range(n):
        for j in range(i + 1, n):
            pom1[i][j] = 1
    print("Wygenerowana macierz sasiedztwa grafu acyklicznego skierowanego: \n")
    for i in range(n):
        print(pom1[i], '\n')