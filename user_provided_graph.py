import os
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
            # próba konwersji do liczb
            try:
                nums_input = [int(tok) for tok in tokens]
            except ValueError:
                print("Podaj ponownie wierzcholki")
                continue
            # sprawdzenie powielenia
            if len(nums_input) != len(set(nums_input)):
                print("Podaj ponownie wierzcholki - powielony wierzchołek")
                continue
            temp = []
            valid = True
            for num in nums_input:
                if num < 1 or num > n or num == i+1 or matrix[i][num-1] != 0:
                    valid = False
                    break
                temp.append(num)
            if not valid:
                print("Podaj ponownie wierzcholki")
                continue
            nums = temp
            break
        if not nums:
            continue

        for num in nums:
            num -= 1
            matrix[i][num] = 1
            matrix[num][i] = -1
    os.system('cls' if os.name=='nt' else 'clear')
    return matrix


