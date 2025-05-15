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
os.system('cls')
print("Witaj w programie!!\n")

while (answer != "wygenerowac" and answer != "wpisac"):
    answer = input("Wybierz odpowiednia opcje:\n-wpisz 'wygenerowac' jesli chcesz wygenerowac spojny acykliczny graf o nasyceniu rownym 50%\n-wpisz 'wpisac' jesli chcesz samemu podac jak wyglada graf\n")
    if (answer != 'wygenerowac' and answer != 'wpisac'): print("Podales niedozwolona wartosc")
os.system('cls')    
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

while answer != 'stop':
    answer = input("\nJaka operacje chcialbys zrobic na grafie:\n-wpisz 'print' jesli wypisac graf\n-wpisz 'breath' jeśli chcesz uzyc metody przeszukiwania wszerz\n-wpisz 'depth' uzyc metody przeszukiwania w glab\n-wpisz 'kahn' jesli sortowanie metoda Kahna\n-wpisz 'tarjan' jesli sortowanie metoda Tarjana\n-wpisz 'stop' jesli chcesz zakonczyc\n")
    if (answer == 'breath'):
        os.system('cls')
        print(width(graph, n))
    elif (answer == 'depth'):
        os.system('cls')
        print(depth_search(graph, n))
    elif (answer == 'kahn'):
        os.system('cls')
        print(kahn(graph, n))
    elif (answer == 'tarjan'):
        os.system('cls')
        Tarjan(graph, n)
    elif(answer == 'print'):
        os.system('cls')
        Print(graph, n)
    elif (answer != 'stop' and answer != 'print' and answer != 'breath' and answer != 'depth' and answer != 'kahn' and answer != 'tarjan'):
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



