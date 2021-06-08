matrix = []
for i in range(8):
    matrix.append(input().split())


def check_valid_move(row_, col_):
    if 0 <= row_ < 8 and 0 <= col_ < 8:
        return True
    return False


def check_up(row_, col_):
    while check_valid_move(row_ - 1, col_) and not matrix[row_ - 1][col_] == "Q":
        if matrix[row_ - 1][col_] == "K":
            return True
        row_ -= 1
    return False


def check_down(row_, col_):
    while check_valid_move(row_ + 1, col_) and not matrix[row_ + 1][col_] == "Q":
        if matrix[row_ + 1][col_] == "K":
            return True
        row_ += 1
    return False


def check_left(row_, col_):
    while check_valid_move(row_, col_ - 1) and not matrix[row_][col_ - 1] == "Q":
        if matrix[row_][col_ - 1] == "K":
            return True
        col_ -= 1
    return False


def check_right(row_, col_):
    while check_valid_move(row_, col_ + 1) and not matrix[row_][col_ + 1] == "Q":
        if matrix[row_][col_ + 1] == "K":
            return True
        col_ += 1
    return False


def check_up_left(row_, col_):
    while check_valid_move(row_ - 1, col_ - 1) and not matrix[row_ - 1][col_ - 1] == "Q":
        if matrix[row_ - 1][col_ - 1] == "K":
            return True
        col_ -= 1
        row_ -= 1
    return False


def check_up_right(row_, col_):
    while check_valid_move(row_ - 1, col_ + 1) and not matrix[row_ - 1][col_ + 1] == "Q":
        if matrix[row_ - 1][col_ + 1] == "K":
            return True
        col_ += 1
        row_ -= 1
    return False


def check_down_left(row_, col_):
    while check_valid_move(row_ + 1, col_ - 1) and not matrix[row_ + 1][col_ - 1] == "Q":
        if matrix[row_ + 1][col_ - 1] == "K":
            return True
        col_ -= 1
        row_ += 1
    return False


def check_down_right(row_, col_):
    while check_valid_move(row_ + 1, col_ + 1) and not matrix[row_ + 1][col_ + 1] == "Q":
        if matrix[row_ + 1][col_ + 1] == "K":
            return True
        col_ += 1
        row_ += 1
    return False


def check_movements(row_, col_):
    if check_up(row_, col_) or check_down(row_, col_) or check_left(row_, col_) or check_right(row_, col_) \
            or check_down_left(row_, col_) or check_down_right(row_, col_) or check_up_left(row_, col_) \
            or check_up_right(row_, col_):
        return True
    return False


killers = []
for row_index in range(8):
    for col_index in range(8):
        if matrix[row_index][col_index] == "Q":
            if check_movements(row_index, col_index):
                killers.append([row_index, col_index])

if not killers:
    print("The king is safe!")
else:
    for killer in killers:
        print(killer)
