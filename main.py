from acyclic_graph import *
from width_search import *
from tarjan_algorithm import *
from user_provided_graph import *

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

if answer == 'wygenerowac':
    saturation = float(input("Podaj nasycenie: "))
    graph = generate(n, saturation)
    print(graph)

elif answer == 'wpisac':
    graph = providing_graph(n)

answer2 = input("Jakim algorytmem chcialbys posortowac graf: \n-Kahna\n-Tarjana\n")
if (answer2 == 'Tarjana'):
    posortowane = Tarjan(graph, n)
    print(posortowane)



