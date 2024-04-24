from typing import Dict, List,Tuple
from math import inf
import networkx as nx
import matplotlib.pyplot as plt

def Bellman_Ford(G: Dict, a: List[List], start: int, end: int) -> Tuple[float, List[int]]:
    d = {i: inf for i in G.keys()} # Odległość od początkowego punktu
    p = {i: -1 for i in G.keys()} # Zbiór poprzedników danych wierzchołków
    d[start] = 0 # Ustawienie odległości od pierwszego wierzchołka na 0

    for _ in range(len(G) - 1): # przechodzimy przez n - 1 wierzchołków
        for u in G.keys():
            for v in G[u]:
                if d[v] > d[u] + a[u][v]: # sprawdzenie warunku czy odległość wierzchołka v jest większa od odległości wierzchołka u + waga krawędzi
                    d[v] = d[u] + a[u][v] # przypisanie odległości jako suma odległości wierzchołka u i funkcji wagowej a{u,v}
                    p[v] = u # ustawienie poprzednika na wierzchołek u

    for u in G.keys():
        for v in G[u]:
            if d[v] > d[u] + a[u][v]: # sprawdzenie ujemnego cyklu
                raise ValueError('Graph has negative cycle') # zwrócenie wyjatku

    path = [] # utworzenie listy odwiedzonych
    v = end
    while v != -1:
        path.append(v) # dodavanie do listy odwiedzonych
        v = p[v]

    return d[end], path[::-1]


graph = {
    0: [1],
    1: [0, 2, 4],
    2: [1, 5, 6],
    3: [0, 4],
    4: [3, 6, 7, 8],
    5: [1],
    6: [2, 7, 9],
    7: [8],
    8: [4, 7],
    9: [7]
}

a = [[inf, 1, inf, inf, inf, inf, inf, inf, inf, inf],
    [1, inf, 3, inf, 3, inf, inf, inf, inf, inf],
    [inf, 3, inf, inf, inf, 2, 1, inf, inf, inf],
    [6, inf, inf, inf, 3, inf, inf, inf, inf, inf],
    [inf, inf, inf, 3, inf, inf, 2, 5, 1, inf],
    [inf, 1, inf, inf, inf, inf, inf, inf, inf, inf],
    [inf, inf, 1, inf, inf, inf, inf, 3, inf, 2],
    [inf, inf, inf, inf, inf, inf, inf, inf, 2, inf],
    [inf, inf, inf, inf, 1, inf, inf, 2, inf, inf],
    [inf, inf, inf, inf, inf, inf, inf, 1, inf, inf]]

result = Bellman_Ford(graph, a, 0, 9)
print("Najkrótsza znaleziona ścieżka ma długość: ", result[0])
print("Ścieżka ta przechodzi przez wierzchołki: ", result[1])

result = Bellman_Ford(graph, a, 1, 8)
print("Najkrótsza znaleziona ścieżka ma długość: ", result[0])
print("Ścieżka ta przechodzi przez wierzchołki: ", result[1])

result = Bellman_Ford(graph, a, 9, 5)
print("Najkrótsza znaleziona ścieżka ma długość: ", result[0])
print("Ścieżka ta przechodzi przez wierzchołki: ", result[1])
# G = nx.DiGraph(graph)
#
# nx.draw(G, with_labels=True)
# plt.show()
