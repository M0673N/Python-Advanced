def read_matrix():
    n = int(input())
    data = []
    for row_ in range(n):
        data.append([int(i) for i in input().split()])
    return data


def explode_bomb(data, row_, col_):
    bomb_strength = data[row_][col_]
    if bomb_strength <= 0:
        return data
    else:
        data[row_][col_] = 0
        data = explode_0(data, row_, col_, bomb_strength)
        data = explode_1(data, row_, col_, bomb_strength)
        data = explode_2(data, row_, col_, bomb_strength)
        data = explode_3(data, row_, col_, bomb_strength)
        data = explode_5(data, row_, col_, bomb_strength)
        data = explode_6(data, row_, col_, bomb_strength)
        data = explode_7(data, row_, col_, bomb_strength)
        data = explode_8(data, row_, col_, bomb_strength)
        return data


def explode_0(data, row_, col_, bomb_strength):
    if row_ >= 1 and col_ >= 1:
        if data[row_ - 1][col_ - 1] > 0:
            data[row_ - 1][col_ - 1] -= bomb_strength
    return data


def explode_1(data, row_, col_, bomb_strength):
    if row_ >= 1:
        if data[row_ - 1][col_] > 0:
            data[row_ - 1][col_] -= bomb_strength
    return data


def explode_2(data, row_, col_, bomb_strength):
    if row_ >= 1 and col_ <= len(data[row_]) - 2:
        if data[row_ - 1][col_ + 1] > 0:
            data[row_ - 1][col_ + 1] -= bomb_strength
    return data


def explode_3(data, row_, col_, bomb_strength):
    if col_ >= 1:
        if data[row_][col_ - 1] > 0:
            data[row_][col_ - 1] -= bomb_strength
    return data


def explode_5(data, row_, col_, bomb_strength):
    if col_ <= len(data[row_]) - 2:
        if data[row_][col_ + 1] > 0:
            data[row_][col_ + 1] -= bomb_strength
    return data


def explode_6(data, row_, col_, bomb_strength):
    if row_ <= len(data) - 2 and col_ >= 1:
        if data[row_ + 1][col_ - 1] > 0:
            data[row_ + 1][col_ - 1] -= bomb_strength
    return data


def explode_7(data, row_, col_, bomb_strength):
    if row_ <= len(data) - 2:
        if data[row_ + 1][col_] > 0:
            data[row_ + 1][col_] -= bomb_strength
    return data


def explode_8(data, row_, col_, bomb_strength):
    if row_ <= len(data) - 2 and col_ <= len(data[row_]) - 2:
        if data[row_ + 1][col_ + 1] > 0:
            data[row_ + 1][col_ + 1] -= bomb_strength
    return data


def print_result(data):
    active, the_sum = find_active_cells(data)
    print(f"Alive cells: {active}")
    print(f"Sum: {the_sum}")
    for i in range(len(data)):
        data[i] = [str(i) for i in data[i]]
    for i in data:
        print(" ".join(i))


def find_active_cells(data):
    active = 0
    the_sum = 0
    for row_ in range(len(data)):
        for col_ in range(len(data[row_])):
            if data[row_][col_] > 0:
                active += 1
                the_sum += data[row_][col_]
    return active, the_sum


matrix = read_matrix()
bombs = [i.split(",") for i in input().split()]
for bomb in bombs:
    row = int(bomb[0])
    col = int(bomb[1])
    matrix = explode_bomb(matrix, row, col)

print_result(matrix)
