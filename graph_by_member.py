def uzytkownik(n):
    pom1 = []
    for i in range(n):
        pom1.append([0]*n)
    for i in range(n):
        for j in range(n):
            print("Aktualna krawedz jest pomiedzy", i + 1, "i", j + 1, "wierzcholkiem wpisz 1 jesli krawedz pomiedzy tymi wierzcholkami lub 0 jesli nie")
            pom1[i][j] = int(input())
    return pom1