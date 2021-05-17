def read_matrix():
    n = int(input())
    movements = input().split()
    data = []
    for row in range(n):
        data.append(input().split())
    return data, movements


def find_miner(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "s":
                position = [row, col]
                return position


def move_miner(data, position, order):
    coal_collected = 0

    if order == "up" and position[0] >= 1:
        if data[position[0] - 1][position[1]] == "c":
            coal_collected += 1
            data[position[0] - 1][position[1]] = "*"
            position[0] -= 1
            return data, position, coal_collected
        else:
            position[0] -= 1
            return data, position, coal_collected

    elif order == "down" and position[0] < len(data) - 1:
        if data[position[0] + 1][position[1]] == "c":
            coal_collected += 1
            data[position[0] + 1][position[1]] = "*"
            position[0] += 1
            return data, position, coal_collected
        else:
            position[0] += 1
            return data, position, coal_collected

    elif order == "left" and position[1] >= 1:
        if data[position[0]][position[1] - 1] == "c":
            coal_collected += 1
            data[position[0]][position[1] - 1] = "*"
            position[1] -= 1
            return data, position, coal_collected
        else:
            position[1] -= 1
            return data, position, coal_collected

    elif order == "right" and position[1] < len(data[position[0]]) - 1:
        if data[position[0]][position[1] + 1] == "c":
            coal_collected += 1
            data[position[0]][position[1] + 1] = "*"
            position[1] += 1
            return data, position, coal_collected
        else:
            position[1] += 1
            return data, position, coal_collected

    return data, position, coal_collected


def find_all_coal(data):
    counter = 0
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "c":
                counter += 1
    return counter


def find_end(data):
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "e":
                position = [row, col]
                return position


matrix, commands = read_matrix()
miner_position = find_miner(matrix)
total_coal = 0
all_coal = find_all_coal(matrix)
end = find_end(matrix)
early_end = False
for command in commands:
    matrix, miner_position, coal = move_miner(matrix, miner_position, command)
    total_coal += coal
    if total_coal == all_coal:
        print(f"You collected all coals! ({miner_position[0]}, {miner_position[1]})")
        early_end = True
        break
    if miner_position == end:
        print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
        early_end = True
        break

if not early_end:
    print(f"{all_coal - total_coal} coals left. ({miner_position[0]}, {miner_position[1]})")
