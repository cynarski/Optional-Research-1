from typing import Dict
from copy import deepcopy
from math import inf

def GTSP(G: Dict, a):

    lst = []
    V = dict()
    path = []
    suma = 0
    for k, v in G.items():
        for i in range(len(v)):
            if (k, v[i]) not in lst:
                lst.append((k, v[i]))
    weight_edges = dict()
    for edge in lst:
        weight_edges[edge] = a[edge[0]][edge[1]]

    new = sorted(weight_edges.items(),key=lambda x: x[1])
    w_copy = deepcopy(a)  # tworzę kopię macierzy a aby nie modyfikować oryginalnej macierzy

    i = 0
    while len(V.keys()) < len(G.keys()):
        if i > len(new) - 1:
            break
        elem = new[i]
        i += 1
        x = elem[0][0]
        y = elem[0][1]

        w_copy[x][y] = inf
        if x in V.keys() or y in V.values():
            continue
        if y in V.keys() and x in V.values() and len(V.keys()) < (len(G.keys()) - 1):
            ans = True
            tmp = y
            for i in range(len(V.keys())):
                if tmp not in V.keys():
                    ans = False
                else:
                    tmp = V[tmp]
            if ans:
                continue

        # Dodaję do słownika V krawędź o kluczu x i wartośći y
        V[x] = y
        suma += a[x][y]

    key = list(V.keys())[0]
    for _ in range(len(V)):
        if key in path:
            raise Exception('Nie ma takiego klucza w ścieżce')
        path.append(key)
        if key not in V.keys():
            break
        else:
            key = V[key]
    if len(path) < len(V.keys()) - 1:
        raise Exception("Błędna scieżka")

    return path, suma

def print_path(arr):
    result = ""
    for i in range(len(arr)):
        result += f"{arr[i]} -> "
    result += f"{arr[0]}"
    return result


graph = {
    0: [1, 2, 3, 4, 5, 6],
    1: [3, 4, 6, 7, 8, 9],
    2: [0, 1, 3, 4, 5, 6, 7, 8, 9],
    3: [0, 1, 2, 4, 5, 6, 7, 8, 9],
    4: [1, 2, 5, 6, 8, 9],
    5: [0, 1, 2, 3, 4, 6, 7, 8, 9],
    6: [0, 1, 2, 4, 5, 7, 8, 9],
    7: [1, 2, 3, 4, 5, 6, 8, 9],
    8: [1, 2, 3, 4, 5, 6, 7],
    9: [2, 3, 4, 5, 6, 7, 8]
}

a = [[inf, -1, 1, 1, 1, 1, 1, inf, inf],
      [inf, inf, 2, 2, 2, 2, 2, 2, 2, -2],
      [1, 2, inf, 3, 3, 3, 3, 3, 3, 3],
      [1, 2, 3, inf, 4, 4, 4, 4, 4, 4],
      [inf, 2, 3, 4, inf, 5, 5, 5, 5, 5],
      [1, 2, 3, 4, 5, inf, 6, 6, 6, 6],
      [1, 2, 3, 4, 5, 6, inf, 7, 7, 7],
      [inf, 2, 3, 4, 5, 6, 7, inf, 8, 8],
      [inf, 2, 3, 4, 5, 6, 7, 8, inf, 9],
      [inf, inf, 3, 4, 5, 6, 7, 8, 9, inf]]

path, suma = GTSP(graph, a)
print(f'Ścieżka: {print_path(path)}')
print(f'Koszt: {suma}')

