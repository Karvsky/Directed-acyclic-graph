def providing_graph(n):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        nums = []

        while True:
            m = input(f"{i+1}: ")
            if m == "":
                break
            tokens = m.split()
            if len(tokens) > n:
                print("Za dużo wierzcholkow")
                continue
            temp = []
            valid = True
            for tok in tokens:
                try:
                    num = int(tok)
                except ValueError:
                    valid = False
                    break
                if num < 1 or num > n or num == i+1 or matrix[i][num-1] != 0:
                    valid = False
                    break
                temp.append(num)
            if not valid:
                print("Podaj ponownie wierzcholki")
                continue
            nums = list(set(temp))
            break
        if not nums:
            continue

        for num in nums:
            num -= 1
            matrix[i][num] = 1
            matrix[num][i] = -1

    for i in range(n):
        print(' '.join(f"{val:3d}" for val in matrix[i]))
        
    return matrix


