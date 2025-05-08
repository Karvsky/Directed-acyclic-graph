def generator(n):
    pom1 = []
    pom2 = 0
    pom3 = 1
    for i in range(n):
        pom1.append([0]*n)
    for i in range(n):
        if (pom3 == 0):
            break
        for j in range(i + 1, n):
            pom1[i][j] = 1
            pom2 += 1
            if (pom2 == (0.5*(n*(n-1)/2))):
                pom3 = 0
                break
    print("Wygenerowana macierz sasiedztwa grafu acyklicznego skierowanego: \n")
    for i in range(n):
        print(pom1[i], '\n')
