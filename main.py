from acyclic_graph import *
from width_search import *
from depth_search import *
from tarjan_algorithm import *
from user_provided_graph import *
from change import *
from kahn_algorithm import *
import os

answer = ''
graph = []
os.system('cls' if os.name=='nt' else 'clear')
print("Witaj w programie!!\n")

while (answer != "wygenerowac" and answer != "wpisac"):
    answer = input("Wybierz odpowiednia opcje:\n-wpisz 'wygenerowac' jesli chcesz wygenerowac spojny acykliczny graf\n-wpisz 'wpisac' jesli chcesz samemu podac jak wyglada graf\n").lower()
    if (answer != 'wygenerowac' and answer != 'wpisac'): print("Podales niedozwolona wartosc")
os.system('cls' if os.name=='nt' else 'clear')    
n = 0
while n < 1:
    try:
        n = int(input("Podaj ilosc wierzcholkow: "))
        if n < 1:
            print("Liczba wierzcholkow musi byc wieksza od 0")
            n = 0
    except ValueError:
        n = 0
        print("Niepoprawna wartosc, podaj liczbe calkowita")
saturation = 101
if answer == 'wygenerowac':
    while saturation < 0 or saturation > 100:
        try:
            saturation = float(input("Podaj nasycenie: "))
            if saturation < 0 or saturation > 100:
                print("Nasycenie musi byc wartoscia pomiedzy 0 a 100")
                saturation = 101
        except ValueError:
            saturation = 101
            print("Niepoprawna wartosc, podaj liczbe calkowita")
    graph = generate(n, saturation)
elif answer == 'wpisac':
    graph = providing_graph(n)

# 2) Wybieramy reprezentację
rep = ''
while rep not in ('matrix','list','table'):
    rep = input("Wybierz reprezentację grafu (matrix/list/table): ").lower()

# 3) Konwertujemy strukturę na wybraną reprezentację
if rep == 'list':
    # Lista sąsiedztwa 1-based
    graph_rep = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1:
                graph_rep[u].append(v+1)
elif rep == 'table':
    # Tabela krawędzi jako lista par (u,v) 1-based
    graph_rep = []
    for u in range(n):
        for v in range(n):
            if graph[u][v] == 1:
                graph_rep.append((u+1, v+1))
else:
    # Macierz sąsiedztwa
    graph_rep = [row[:] for row in graph]  # macierz jako jest

while True:
    answer = input("\nJaka operacje chcialbys zrobic na grafie:\n-wpisz 'print' jesli wypisac graf\n-wpisz 'find' jesli chcesz znalezc krawedz\n-wpisz 'breath' jeśli chcesz uzyc metody przeszukiwania wszerz\n-wpisz 'depth' uzyc metody przeszukiwania w glab\n-wpisz 'kahn' jesli sortowanie metoda Kahna\n-wpisz 'tarjan' jesli sortowanie metoda Tarjana\n-wpisz 'stop' jesli chcesz zakonczyc\n").lower()
    if (answer == 'breath'):
        os.system('cls' if os.name=='nt' else 'clear')
        print(width(graph, n))
    elif (answer == 'depth'):
        os.system('cls' if os.name=='nt' else 'clear')
        print(depth_search(graph, n))
    elif (answer == 'kahn'):
        os.system('cls' if os.name=='nt' else 'clear')
        print(kahn(graph_rep, n, rep))
    elif (answer == 'tarjan'):
        os.system('cls' if os.name=='nt' else 'clear')
        print(Tarjan(graph_rep, n, rep))
    elif(answer == 'print'):
        os.system('cls' if os.name=='nt' else 'clear')
        # print all representations from original adjacency matrix
        Print(graph, n)
    elif(answer == 'find'):
        os.system('cls' if os.name=='nt' else 'clear')
        # use chosen representation to find edge
        find(graph_rep, n, rep)
    elif(answer == 'stop'):
        break
    else:
        print("Podales niepoprawna wartosc. Napisz jeszcze raz")
print(""" 
      _______~
   .'         '.
  /   O     O   \\
 |      ^        |
 |    \\___/      |
  \\             /
   '._________. '
      """)



