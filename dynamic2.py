# + własny przykład
import numpy as np
from math import inf


def WPP(g, h, q, ymin, ymax, beg, end):
    # g - koszt produkcji
    # h - koszt składowania po rozpatrywanym kresie
    # Ymax - pojemność maksymalna magazynu
    # Ymin - pojemność minimalna magazynu
    # beg - stan początkowy
    # stan końcowy
    b = ymax - ymin
    X = np.zeros((b + 1, len(q)))
    f = np.full((b + 1, len(q)), np.inf)

    for y in range(f.shape[0]):
        x = q[f.shape[1] - 1][0] - (ymin + y) + end
        if x < 0 or x > ymax:
            X[y][0] = None
            f[y][0] = inf
        else:
            X[y][0] = x
            f[y][0] = g[x] + ymin

    counter = f.shape[1] - 2
    for i in range(1, f.shape[1] - 1):
        for y in range(f.shape[0]):
            idx_down = max(q[counter][0] - y, 0)
            idx_up = min(ymax + q[counter][0] - (ymin + y), len(g) - 1)
            newlist = [m for m in range(ymax + 2) if idx_down <= m <= idx_up]
            mini = inf
            x_mini = 0
            for x in newlist:
                f[y][i] = g[x][0] + h[y + x - q[counter][0]][0] + f[y + x - q[counter][0]][i - 1]
                if f[y][i] < mini:
                    mini = f[y][i]
                    x_mini = x
            if idx_down > idx_up or idx_up < 0 or idx_down < 0 or idx_up > len(g) - 1:
                X[y][i] = None
                f[y][i] = inf
            else:
                X[y][i] = x_mini
                f[y][i] = mini
        counter -= 1

    for y in range(f.shape[0]):
        if y == beg - ymin:
            idx_down = max(q[counter][0] - y, 0)
            idx_up = min(ymax + q[counter][0] - (ymin + y), len(g) - 1)
            newlist = [m for m in range(ymax + 2) if idx_down <= m <= idx_up]
            mini = inf
            x_mini = 0
            for x in newlist:
                f[y][f.shape[1] - 1] = g[x] + h[y + x - q[counter][0]][0] + f[y + x - q[counter][0]][f.shape[1] - 2]
                if f[y][f.shape[1] - 1] < mini:
                    mini = f[y][f.shape[1] - 1]
                    x_mini = x
            if idx_down > idx_up or idx_up < 0 or idx_down < 0 or idx_up > len(g) - 1:
                X[y][f.shape[1] - 1] = None
                f[y][f.shape[1] - 1] = inf
            else:
                X[y][f.shape[1] - 1] = x_mini
                f[y][f.shape[1] - 1] = mini
        else:
            X[y][f.shape[1] - 1] = None
            f[y][f.shape[1] - 1] = inf
    return X, f


def strategy(q, ymin, beg, X, f):
    yik = beg
    strat = ''
    for i in range(f.shape[1] - 1, -1, -1):
        idx = f.shape[1] - i - 1
        strat += f"x{idx + 1} --> {int(X[yik - ymin, i])}\n y{idx} --> {yik}\n f{len(q) - 1 - idx + 1}(y{idx}) = {f[yik - ymin, i]}\n\n"
        yik = int(yik + int(X[yik - ymin, i]) - q[idx][0])

    strat += f"Koszt całkowity: {f[beg - ymin, f.shape[1] - 1]}\n"
    return strat

def get_results(q, y_min, y_begining, x_matrix, f):
    state = y_begining
    strategy = f"Koszt całkowity = {f[y_begining - y_min, -1]}\n"

    for j in range(f.shape[1] - 1, -1, -1):
        input_index = f.shape[1] - j - 1
        decision = int(x_matrix[state - y_min, j])
        strategy += f"|y{input_index} = {state}, x{input_index} = {decision}|\n"
        state = int(state + decision - q[input_index])
    strategy += f"|y{len(q)} = {state}|\n"

    return strategy
# |y0 = 0, x0 = 4|
# |y1 = 1, x1 = 5|
# |y2 = 3, x2 = 0|
# |y3 = 0, x3 = 4|
# |y4 = 1, x4 = 5|
# |y5 = 3, x5 = 0|
# |y6 = 0|

# g = np.array([[0],
#               [15],
#               [18],
#               [19],
#               [20],
#               [24]])
#
# h = np.array([[i * 2] for i in range(6)])
#
# q = np.array([[3],
#               [3],
#               [3],
#               [3],
#               [3],
#               [3]])
#
# Ymax = 4  # Y - pojemność magazynu maksymalna
# Ymin = 0  # ymin- pojemność magazynu minimalna
#
# beg = 0
# end = 0
#
# g = np.array([[2],
#               [8],
#               [12],
#               [15],
#               [17],
#               [20]])
#
# h = np.array([[1],
#               [2],
#               [2],
#               [4]])
#
# q = np.array([[4],
#               [2],
#               [6],
#               [5]])
#
# Ymin = 2
# Ymax = 5
# beg = 4
# end = 3


g = np.array([[1],[3],[5],[15],[20],[22],[25],[30],[39]])

h = np.array([[1],[2],[6],[10],[14],[20],[27]])

q = [[3],[2],[7],[5],[8],[7],[4],[2],[3],[10],[3],[8]]

Ymin = 2
Ymax = 7
beg = 7
end = 2
# #\

# q = [[8],
#      [2],
#      [10],
#      [3]]
#
# h = np.array([[1],
#               [7],
#               [3],
#               [4],
#               [6],
#               [5],
#               [2]])
#
# g = np.array([[2],
#               [4],
#               [7],
#               [14],
#               [23],
#               [33],
#               [36],
#               [47]])
#
# Ymin = 2
# Ymax = 6
# beg = 5
# end = 3

if __name__ == '__main__':
    X, f = WPP(g, h, q, Ymin, Ymax, beg, end)
    #
    print(f"Macierz xi  \n{X}\n\nMacierz f(yi) \n{f}")
    q = [3,2,7,5,8,7,4,2,3,10,3,8]
    # q = [4,2,6,5]
    print("\nOptymalna strategia\n", get_results(q, Ymin, beg, X, f))
