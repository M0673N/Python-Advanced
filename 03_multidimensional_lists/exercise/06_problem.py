def read_matrix():
    n = int(input())
    data = []
    for row in range(n):
        data.append([i for i in input()])
    return data


def find_knights(data):
    knights_ = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "K":
                knights_.append([row, col, 0])
    return knights_


def check_up_left(data, row_, col_):
    if row_ > 1 and col_ > 0:
        if data[row_ - 2][col_ - 1] == "K":
            return 1
    return 0


def check_up_right(data, row_, col_):
    if row_ > 1 and col_ < len(data) - 1:
        if data[row_ - 2][col_ + 1] == "K":
            return 1
    return 0


def check_left_up(data, row_, col_):
    if row_ > 0 and col_ > 1:
        if data[row_ - 1][col_ - 2] == "K":
            return 1
    return 0


def check_left_down(data, row_, col_):
    if row_ < len(data) - 1 and col_ > 1:
        if data[row_ + 1][col_ - 2] == "K":
            return 1
    return 0


def check_right_up(data, row_, col_):
    if row_ > 0 and col_ < len(data) - 2:
        if data[row_ - 1][col_ + 2] == "K":
            return 1
    return 0


def check_right_down(data, row_, col_):
    if row_ < len(data) - 1 and col_ < len(data) - 2:
        if data[row_ + 1][col_ + 2] == "K":
            return 1
    return 0


def check_down_left(data, row_, col_):
    if row_ < len(data) - 2 and col_ > 0:
        if data[row_ + 2][col_ - 1] == "K":
            return 1
    return 0


def check_down_right(data, row_, col_):
    if row_ < len(data) - 2 and col_ < len(data) - 1:
        if data[row_ + 2][col_ + 1] == "K":
            return 1
    return 0


def calculate_aggression(data, knight_):
    row = knight_[0]
    col = knight_[1]
    counter = 0
    counter += check_up_left(data, row, col)
    counter += check_up_right(data, row, col)
    counter += check_left_up(data, row, col)
    counter += check_left_down(data, row, col)
    counter += check_right_up(data, row, col)
    counter += check_right_down(data, row, col)
    counter += check_down_left(data, row, col)
    counter += check_down_right(data, row, col)
    knight_[2] = counter
    return knight_


matrix = read_matrix()
knights = find_knights(matrix)
aggressive_knights = []
for knight in knights:
    aggressive_knights.append(calculate_aggression(matrix, knight))
aggressive_knights.sort(key=lambda x: -x[2])
removed = 0
while aggressive_knights[0][2] > 0:
    bad_row = aggressive_knights[0][0]
    bad_col = aggressive_knights[0][1]
    matrix[bad_row][bad_col] = "0"
    removed += 1
    knights = find_knights(matrix)
    aggressive_knights = []
    for knight in knights:
        aggressive_knights.append(calculate_aggression(matrix, knight))
    aggressive_knights.sort(key=lambda x: -x[2])
print(removed)
