from typing import Dict, List
from math import inf
import networkx as nx
import matplotlib.pyplot as plt


def DPA(G: Dict, a, s: int):
    # stowrzenie zmiennych A, suma alfa,beta i Q - punkty 1 do 6
    A = list()
    suma = 0
    alfa = [0 for _ in range(len(G))]
    beta = [inf for _ in range(len(G))]
    Q = [i for i in range(len(G))]
    #zdjecie z Q wierzchołka s i przypisane mu wartości )
    beta[s] = 0
    Q.remove(s)

    u_last = s

    while Q: # petla główna
        for _ in Q:
            for u in G[u_last]: # dla każdego (u ∈ Q i u ∈ N[u*])
                # jeśli a[u,u*]<beta[u] to alfa[u] ←u*; beta[u]←a[u,u*]
                if a[u][u_last] < beta[u]:
                    alfa[u] = u_last
                    beta[u] = a[u][u_last]

        arg_min = inf
        for u in Q: # dla każdego u ∈ Q
            if beta[u] < arg_min:
                arg_min = beta[u]
                u_last = u

        Q.remove(u_last) # Q ← Q-{u*}
        A.append((alfa[u_last], u_last)) # A ← A+{alfa[u*],u*}
        suma += a[alfa[u_last]][u_last] # suma ← suma + a[alfa[u*],u*]

    return A, suma


graph = {
    0: [1, 4, 5],
    1: [4, 5, 8],
    2: [0, 9],
    3: [5, 9],
    4: [0, 1, 2, 8],
    5: [0, 1, 3],
    6: [7, 8, 9],
    7: [6, 8, 9],
    8: [1, 4, 6, 7],
    9: [2, 3, 5, 6]
}

a = [[inf, 2, inf, inf, 3, 4, inf, inf, inf, inf],
     [inf, inf, inf, inf, 2, 8, inf, inf, 8, inf],
     [1, inf, inf, inf, inf, inf, inf, inf, inf, 7],
     [inf, inf, inf, inf, inf, 1, inf, inf, inf, 2],
     [3, 2, 6, inf, inf, inf, inf, inf, 1, inf],
     [4, 8, inf, 1,inf, inf, inf, inf, inf, inf],
     [inf, inf, inf, inf, inf, inf, inf, 4, 3, 2],
     [inf, inf, inf, inf, inf,inf, 4, inf, 4, 1],
     [inf, 8, inf, inf, 1, inf, 3, 4, inf, inf],
     [inf, inf, 7, 2, inf, 5, 2, inf, inf, inf]
     ]

# G = nx.DiGraph(graph)
#
# nx.draw(G, with_labels=True,node_color='lightblue')
# plt.show()
G1 = {
    0: [1, 2, 3, 4],
    1: [3, 6],
    2: [0, 3, 4, 5],
    3: [0, 1, 2, 5, 6],
    4: [0, 2, 5],
    5: [2, 3, 4, 6],
    6: [1, 3, 5]
}

a1 = [[inf, 2, 1, 4, 3, inf, inf],
     [inf, inf, inf, 3, inf, inf, 5],
     [1, inf, inf, 7, 1, 2, inf],
     [4, 3, 7, inf, inf, 4, 4],
     [3, inf, 1, inf, inf, 3, inf],
     [inf, inf, 2, 4, 3, inf, 3],
     [inf, 5, inf, 4, inf, 3, inf]]
# print(DPA(G1,a1,1))

G2 = {
    0: [1],
    1: [0, 2, 3],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7, 9],
    7: [6, 8],
    8: [7, 9],
    9: [6, 8]
}

a2 = [[inf, 1, inf, inf, inf, inf, inf, inf, inf, inf],
      [1, inf, 3, 5, inf, inf, inf, inf, inf, inf],
      [inf, 3, inf, 4, inf, inf, inf, inf, inf, inf],
      [inf, 5, 4, 2, 7, inf, inf, inf, inf, inf],
      [inf, inf, inf, 2, inf, 1, inf, inf, inf, inf],
      [inf, inf, inf, 7, 1, inf, inf, inf, inf, inf],
      [inf, inf, inf, inf, inf, inf, inf, 1, inf, 2],
      [inf, inf, inf, inf, inf, inf, 1, inf, 4, inf],
      [inf, inf, inf, inf, inf, inf, inf, 4, inf, 3],
      [inf, inf, inf, inf, inf, inf, 2, inf, 3, inf]]


