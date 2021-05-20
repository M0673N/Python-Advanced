def read_matrix():
    rows = int(input())
    data = []
    for row_ in range(rows):
        data.append(list(map(int, input().split())))
    return data


def add(data, row_, col_, value_):
    if 0 <= row_ < len(data) and 0 <= col_ < len(data):
        data[row_][col_] += value_
    else:
        print("Invalid coordinates")
    return data


def subtract(data, row_, col_, value_):
    if 0 <= row_ < len(data) and 0 <= col_ < len(data):
        data[row_][col_] -= value_
    else:
        print("Invalid coordinates")
    return data


def get_tokens(data):
    data = data.split()
    action_ = data[0]
    row_ = int(data[1])
    col_ = int(data[2])
    value_ = int(data[3])
    return action_, row_, col_, value_


matrix = read_matrix()
while True:
    command = input()
    if command == "END":
        break

    action, row, col, value = get_tokens(command)

    if action == "Add":
        matrix = add(matrix, row, col, value)
    elif action == "Subtract":
        matrix = subtract(matrix, row, col, value)

matrix = [[str(col) for col in row] for row in matrix]
[print(" ".join(row)) for row in matrix]
