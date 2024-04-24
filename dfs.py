from typing import Dict,List

def dfs(G:Dict[int,List[int]],s:int):

    No = []

    cycle_exist = False

    is_consistent = True

    stack = []
    stack.append(s)
    while stack:
        v = stack.pop()

        if v not in No:
            No.append(v)
            no_of_neighbours_visited = 0
            for u in G[v][::-1]:
                stack.append(u)
                if u in No:
                    no_of_neighbours_visited += 1
                    if no_of_neighbours_visited > 1:
                        cycle_exist = True

    if len(No) < len(G.keys()):

        is_consistent = False

    return No,cycle_exist,is_consistent


graph = {
    1: [2],
    2: [1, 3],
    3: [2, 7],
    4: [5, 7],
    5: [4, 6],
    6: [5],
    7: [3, 4, 8, 9],
    8: [7, 9],
    9: [7, 8, 10],
    10: [9]
}

sa = {
    1: [2],
    2: [1, 3, 4],
    3: [2],
    4: [2, 5],
    5: [4, 6],
    6: [5]
}

sc = {
    1: [2],
    2: [1, 3, 4],
    3: [2, 5, 6],
    4: [2, 5],
    5: [3, 4, 6],
    6: [3, 5]
}

ac = {
    1: [2],
    2: [1, 4],
    3: [5, 6],
    4: [2],
    5: [3, 6],
    6: [3, 5]
}
graph1 = {1: [2], 2: [3, 4], 3: [2, 4], 4: [2, 3, 5, 6], 5: [4, 6, 10], 6: [4, 5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10],
         10: [5, 9]}

# print(dfs(graph, 3))
# print(DFS(graph, 3))
# ans1 = dfs(sa, 4)
#
# wynik1 = "1: " + str(ans1[0][0])
# for i in range(1, len(ans1[0])):
#     wynik1 += ", " + str(i+1) + ": " + str(ans1[0][i])
#
# wynik1 += "\nCycle exists: " + str(ans1[1])
# wynik1 += "\nGraph is consistent: " + str(ans1[2])
#
# print(wynik1)
#
# ans2 = dfs(sc, 4)
#
# wynik2 = "1: " + str(ans2[0][0])
# for i in range(1, len(ans2[0])):
#     wynik2 += ", " + str(i+1) + ": " + str(ans2[0][i])
#
# wynik2 += "\nCycle exists: " + str(ans2[1])
# wynik2 += "\nGraph is consistent: " + str(ans2[2])
#
# print(wynik2)
#
# ans3 = dfs(ac, 5)
#
# wynik3 = "1: " + str(ans3[0][0])
# for i in range(1, len(ans3[0])):
#     wynik3 += ", " + str(i+1) + ": " + str(ans3[0][i])
#
# wynik3 += "\nCycle exists: " + str(ans3[1])
# wynik3 += "\nGraph is consistent: " + str(ans3[2])
#
# print(wynik3)

ans4 = dfs(graph1,1)
wynik4 = "1: " + str(ans4[0][0])
for i in range(1, len(ans4[0])):
    wynik4 += ", " + str(i+1) + ": " + str(ans4[0][i])

wynik4 += "\nCycle exists: " + str(ans4[1])
wynik4 += "\nGraph is consistent: " + str(ans4[2])

print(wynik4)