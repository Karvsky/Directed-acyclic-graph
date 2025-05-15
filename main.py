from acyclic_graph import *
from width_search import *
from tarjan_algorithm import *
from user_provided_graph import *
from change import *

answer = ''
graph = []
print("Witaj w programie!!\n")

while (answer != "wygenerowac" and answer != "wpisac"):
    answer = input("Wybierz odpowiednia opcje:\n-wpisz 'wygenerowac' jesli chcesz wygenerowac spojny acykliczny graf o nasyceniu rownym 50%\n-wpisz 'wpisac' jesli chcesz samemu podac jak wyglada graf\n")
    if (answer != 'wygenerowac' and answer != 'wpisac'): print("Podales niedozwolona wartosc")
    
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

while answer != 'Stop':
    answer = input("Jaka operacje chcialbys zrobic na grafie:\n-wpisz Print jesli wypisac graf\n-wpisz Breath jeśli chcesz uzyc metody przeszukiwania wszerz\n-wpisz Depth uzyc metody przeszukiwania w glab\n-wpisz Kahna jesli sortowanie metoda Kahna\n-wpisz Tarjana jesli sortowanie metoda Tarjana\n-wpisz Stop jesli chcesz zakonczyc\n")
    if (answer == 'Breath'):
        print(width(graph, n))
    elif (answer == 'Depth'):
        print('jeden jest mistrz polski-Lech')
    elif (answer == 'Kahna'):
        print('naajak byczku')
    elif (answer == 'Tarjana'):
        print(Tarjan(graph, n))
    elif(answer == 'Print'):
        print(Print(graph, n))
    elif (answer != 'Stop' and answer != 'Print' and answer != 'Breath' and answer != 'Depth' and answer != 'Kahna' and answer != 'Tarjana'):
        print("Podales niepoprawna wartosc. Napisz jeszcze raz")
print(""" 
      _______
   .'         '.
  /   O     O   \\
 |      ^        |
 |    \\___/      |
  \\             /
   '._________. '
      """)



