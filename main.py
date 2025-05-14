from acyclic_graph import *
from width_search import *
from tarjan_algorithm import *

answer = ''
graph = []
print("Witaj w programie!!")
while (answer != "wygenerowac" and answer != "wpisac"):
    answer = input("Wybierz odpowiednia opcje:\n-wpisz 'wygenerowac' jesli chcesz wygenerowac spojny acykliczny graf o nasyceniu rownym 50%\n-wpisz 'wpisac' jesli chcesz samemu podac jak wyglada graf\n")
    if (answer != 'wygenerowac' and answer != 'wpisac'):
        print("Podales niedozwolona wartosc")
n = int(input("Podaj liczbe wierzcholkow grafu: "))
if answer == 'wygenerowac':
    saturation = float(input("Podaj nasycenie: "))
    graph = generate(n, saturation)
    print(graph)
answer2 = input("Jakim algorytmem chcialbys posortowac graf: \n-Kahna\n-Tarjana\n")
if (answer2 == 'Tarjana'):
    posortowane = Tarjan(graph, n)
    print(posortowane)



