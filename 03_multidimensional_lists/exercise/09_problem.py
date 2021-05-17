def read_matrix_2():
    rows, columns = map(int, input().split())
    data = []
    for row in range(rows):
        data.append([i for i in input()])
    return data


def find_player(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "P":
                position = [row, col]
                return position


def multiply_bunnies(data, player):
    dead = False
    bunnies = []
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "B":
                bunnies.append([row, col])

    for bunny in bunnies:
        row = bunny[0]
        col = bunny[1]

        if (row < len(data) - 1 and [row + 1, col] == player) \
                or (row >= 1 and [row - 1, col] == player) \
                or (col < len(data[row]) - 1 and [row, col + 1] == player) \
                or (col >= 1 and [row, col + 1] == player):
            dead = True

        if row < len(data) - 1:
            data[row + 1][col] = "B"
        if row >= 1:
            data[row - 1][col] = "B"
        if col < len(data[row]) - 1:
            data[row][col + 1] = "B"
        if col >= 1:
            data[row][col - 1] = "B"

    return data, dead


def move_player(data, place, direction):
    escaped = False
    if direction == "U":
        if place[0] >= 1:
            place[0] -= 1
        else:
            escaped = True
            return place, escaped

    elif direction == "D":
        if place[0] < len(data) - 1:
            place[0] += 1
        else:
            escaped = True
            return place, escaped

    elif direction == "L":
        if place[1] >= 1:
            place[1] -= 1
        else:
            escaped = True
            return place, escaped

    elif direction == "R":
        if place[1] < len(data[place[0]]) - 1:
            place[1] += 1
        else:
            escaped = True
            return place, escaped

    return place, escaped


def print_result(data):
    for row in data:
        print("".join(row))


matrix = read_matrix_2()
directions = [i for i in input()]
location = find_player(matrix)
matrix[location[0]][location[1]] = "."
for move in directions:
    location, ran_away = move_player(matrix, location, move)
    matrix, killed = multiply_bunnies(matrix, location)
    if ran_away:
        print_result(matrix)
        print(f"won: {location[0]} {location[1]}")
        break
    if matrix[location[0]][location[1]] == "B":
        print_result(matrix)
        print(f"dead: {location[0]} {location[1]}")
        break
    if killed:
        print_result(matrix)
        print(f"dead: {location[0]} {location[1]}")
        break
