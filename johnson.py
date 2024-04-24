import numpy as np
from copy import deepcopy
from math import inf

def johnson2(matrix, n=2):

    first = 0
    last = -1
    cross = []
    result_matrix = np.zeros(matrix.shape)

    for k in range(len(matrix[0])):
        min_in_matrix = inf
        for i in range(2):
            for j in range(len(matrix[0])):
                if matrix[i][j] < min_in_matrix and j not in cross:
                    min_in_matrix = matrix[i][j]
                    min_adress = (i, j)

        # dodawanie na początek
        if min_adress[0] == 0:
            result_matrix[0][first] = int(matrix[0][min_adress[1]])
            result_matrix[1][first] = int(matrix[1][min_adress[1]])
            first += 1
            cross.append(min_adress[1])
        # dodawanie na koniec
        elif min_adress[0] == 1:
            result_matrix[0][last] = int(matrix[0][min_adress[1]])
            result_matrix[1][last] = int(matrix[1][min_adress[1]])
            last -= 1
            cross.append(min_adress[1])
    if n == 3:
        return result_matrix
    # obliczanie czasów
    result_to_time = deepcopy(result_matrix)
    result_to_time[1][0] += result_to_time[0][0]
    for i in range(len(result_to_time[0])):
        if i != 0:
            result_to_time[0][i] += result_to_time[0][i -1]
            result_to_time[1][i] += max(result_to_time[0][i], result_to_time[1][i -1])

    return result_matrix, result_to_time

def johnson3(matrix):
    x,y = matrix.shape
    result_matrix = np.zeros((x+2,y))
    temp_matrix = np.array([matrix[0] + matrix[1], matrix[1] + matrix[2]])
    johnosn_help = johnson2(temp_matrix, n=3)
    matrix = np.vstack((matrix,temp_matrix)) # dodawanie wierszy do macierzy
    lst = []
    for i in range(len(johnosn_help[0])):
        for j in range(len(johnosn_help[0])):
            if johnosn_help[0][i] == matrix[3][j] and johnosn_help[1][i] == matrix[4][j]:
                result_matrix[:,j] = matrix[:, i]

    result_matrix = result_matrix[0:3, :]
    result_to_time = deepcopy(result_matrix)
    for i in range(1,len(result_matrix[0])):
        result_to_time[0][i] = result_to_time[0][i-1] + result_matrix[0][i]
    result_to_time[1][0] += int(result_to_time[0][0])
    result_to_time[2][0] += int(result_to_time[1][0])
    for i in range(len(result_to_time[0])):
        if i != 0:
            result_to_time[1][i] += max(result_to_time[0][i], result_to_time[1][i - 1])
    for i in range(len(result_to_time[0])):
        if i != 0:
            result_to_time[2][i] += max(result_to_time[1][i], result_to_time[2][i - 1])

    return result_matrix, result_to_time


matrix = np.array([[9, 6, 8, 7, 12, 3],
                  [7, 3, 5, 10, 4, 7]])

t1 = np.array([[7, 11, 8, 7, 6],
               [6, 5, 3, 5, 3],
               [4, 12, 7, 8, 3]])
print()


print("Macierz początkowa")
matrix_2 = np.array([[34, 18, 74, 43, 8, 81, 84, 16, 68, 48],
                     [49, 5, 22, 21, 86, 5, 44, 32, 12, 83]])

matrix_3 = np.array([[92, 96, 14, 24, 47, 24, 10, 98, 15, 71],
               [89, 49, 79, 43, 5, 47, 9, 71, 4, 77],
               [78, 91, 6, 66, 90, 11, 98, 1, 27, 52]])

print()
print(matrix_3)
print()

print("Macierz po przestawieniach zadań")
print(johnson3(matrix_3)[0])
print()
print("Macierz terminów")
print(johnson3(matrix_3)[1])
print()
print("Kolejność zadań: Z5 -> Z6 -> Z8 -> Z4 -> Z3 -> Z10 -> Z1 -> Z9 -> Z2 -> Z7")
print()
print(f"Minimalny potrzebny czas: {int(johnson3(matrix_3)[1][2][-1])}")

