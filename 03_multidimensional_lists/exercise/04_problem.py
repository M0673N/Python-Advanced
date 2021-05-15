def read_matrix_2():
    rows, columns = map(int, input().split())
    data = []
    for row in range(rows):
        data.append([i for i in input().split()])
    return data


def swap(data, action):
    tokens = action.split()
    if tokens[0] == "swap":
        if len(tokens) == 5:
            from_row = int(tokens[1])
            to_row = int(tokens[3])
            from_col = int(tokens[2])
            to_col = int(tokens[4])
            if from_row < len(data) and to_row < len(data) \
                    and from_col < len(data[from_row]) and to_col < len(data[to_row]):
                data[from_row][from_col], data[to_row][to_col] = data[to_row][to_col], data[from_row][from_col]
                return [" ".join(i) for i in data]
    return False


def print_result(info):
    if not info:
        print("Invalid input!")
    else:
        for formatted_row in info:
            print(formatted_row)


matrix = read_matrix_2()
command = input()
while not command == "END":
    result = swap(matrix, command)
    print_result(result)
    command = input()
