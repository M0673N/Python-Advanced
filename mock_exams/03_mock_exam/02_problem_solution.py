string = input()
n = int(input())


def build_field(num):
    field_ = []
    for row in range(num):
        field_.append([i for i in input()])
    return field_


def locate_player(field_data):
    for row_index in range(len(field_data)):
        for col_index in range(len(field_data[row_index])):
            if field_data[row_index][col_index] == "P":
                field_data[row_index][col_index] = "-"
                return [row_index, col_index]


def move_player(order, field_data, letters, location):
    if order == "up":
        if location[0] - 1 < 0:
            letters = letters[:-1]
        else:
            if not field_data[location[0] - 1][location[1]] == "-":
                letters += field_data[location[0] - 1][location[1]]
                field_data[location[0] - 1][location[1]] = "-"
                location[0] -= 1
            else:
                location[0] -= 1

    elif order == "down":
        if location[0] + 1 > len(field_data) - 1:
            letters = letters[:-1]
        else:
            if not field_data[location[0] + 1][location[1]] == "-":
                letters += field_data[location[0] + 1][location[1]]
                field_data[location[0] + 1][location[1]] = "-"
                location[0] += 1
            else:
                location[0] += 1

    elif order == "left":
        if location[1] - 1 < 0:
            letters = letters[:-1]
        else:
            if not field_data[location[0]][location[1] - 1] == "-":
                letters += field_data[location[0]][location[1] - 1]
                field_data[location[0]][location[1] - 1] = "-"
                location[1] -= 1
            else:
                location[1] -= 1

    elif order == "right":
        if location[1] + 1 > len(field_data[location[1]]) - 1:
            letters = letters[:-1]
        else:
            if not field_data[location[0]][location[1] + 1] == "-":
                letters += field_data[location[0]][location[1] + 1]
                field_data[location[0]][location[1] + 1] = "-"
                location[1] += 1
            else:
                location[1] += 1

    return field_data, letters, location


def print_matrix(data):
    for row in data:
        print("".join(row))


field = build_field(n)
position = locate_player(field)

m = int(input())
for i in range(m):
    command = input()
    field, string, position = move_player(command, field, string, position)

field[position[0]][position[1]] = "P"
print(string)
print_matrix(field)
