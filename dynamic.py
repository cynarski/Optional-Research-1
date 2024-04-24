import numpy as np

def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items


# Przykładowe dane
values = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
weights = [2, 3, 5, 11, 7, 6, 3, 9, 4, 2]
capacity = 25

# Zadanie 1: Wywołanie metod programowania dynamicznego
max_value_01, selected_items_01 = knapsack_01(values, weights, capacity)

# Zadanie 2: Wyświetlanie macierzy decyzji optymalnych i wartości funkcji celu

# Macierz decyzji optymalnych dla Binarnego 0-1 KP
print("Macierz decyzji optymalnych dla Binarnego 0-1 KP:")
dp_01 = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
for i in range(1, len(values) + 1):
    for j in range(1, capacity + 1):
        if weights[i - 1] <= j:
            dp_01[i][j] = max(values[i - 1] + dp_01[i - 1][j - weights[i - 1]], dp_01[i - 1][j])
        else:
            dp_01[i][j] = dp_01[i - 1][j]

selected_items_01 = []
i = len(values)
j = capacity
while i > 0 and j > 0:
    if dp_01[i][j] != dp_01[i - 1][j]:
        selected_items_01.append(i - 1)
        j -= weights[i - 1]
    i -= 1

selected_items_01.reverse()
print("Przedmioty wybrane do plecaka:", selected_items_01)

# Wartość funkcji celu dla Binarnego 0-1 KP
print("Wartość funkcji celu dla Binarnego 0-1 KP:", dp_01[-1][-1])

print("Macierz decyzji optymalnych dla Binarnego 0-1 KP:")
dp_01 = [[0 for _ in range(capacity + 1)] for _ in range(len(values) + 1)]
for i in range(1, len(values) + 1):
    for j in range(1, capacity + 1):
        if weights[i - 1] <= j:
            dp_01[i][j] = max(values[i - 1] + dp_01[i - 1][j - weights[i - 1]], dp_01[i - 1][j])
        else:
            dp_01[i][j] = dp_01[i - 1][j]
print()
matrix = np.array(dp_01)
np.set_printoptions(linewidth=np.inf)
print(matrix)