matrix = []
for i in range(5):
    matrix.append(input().split())


def find_player(data):
    for row_index in range(len(data)):
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] == "A":
                return [row_index, col_index]


def check_if_move_is_valid(data, row_, col_):
    if 0 <= row_ <= len(data) - 1 and 0 <= col_ <= len(data) - 1:
        if data[row_][col_] == ".":
            return True
    return False


def shoot(data, row_, col_, direction_):
    if direction_ == "up":
        row_ -= 1
        while 0 <= row_ <= len(data) - 1 and 0 <= col_ <= len(data) - 1:
            if data[row_][col_] == "x":
                return [row_, col_]
            row_ -= 1
    elif direction_ == "down":
        row_ += 1
        while 0 <= row_ <= len(data) - 1 and 0 <= col_ <= len(data) - 1:
            if data[row_][col_] == "x":
                return [row_, col_]
            row_ += 1
    elif direction_ == "left":
        col_ -= 1
        while 0 <= row_ <= len(data) - 1 and 0 <= col_ <= len(data) - 1:
            if data[row_][col_] == "x":
                return [row_, col_]
            col_ -= 1
    elif direction_ == "right":
        col_ += 1
        while 0 <= row_ <= len(data) - 1 and 0 <= col_ <= len(data) - 1:
            if data[row_][col_] == "x":
                return [row_, col_]
            col_ += 1
    return False


def check_for_targets(data):
    targets = 0
    for row_index in range(len(data)):
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] == "x":
                targets += 1
    return targets


targets_in_the_beginning = check_for_targets(matrix)
targets_shot = 0
player_position = find_player(matrix)
matrix[player_position[0]][player_position[1]] = "."
shot_targets_locations = []
n = int(input())
for i in range(n):
    info = input().split()
    command = info[0]
    direction = info[1]
    if command == "move":
        amount = int(info[2])
        if direction == "up":
            if check_if_move_is_valid(matrix, player_position[0] - amount, player_position[1]):
                player_position[0] -= amount
        elif direction == "down":
            if check_if_move_is_valid(matrix, player_position[0] + amount, player_position[1]):
                player_position[0] += amount
        elif direction == "left":
            if check_if_move_is_valid(matrix, player_position[0], player_position[1] - amount):
                player_position[1] -= amount
        elif direction == "right":
            if check_if_move_is_valid(matrix, player_position[0], player_position[1] + amount):
                player_position[1] += amount
    elif command == "shoot":
        shot_result = shoot(matrix, player_position[0], player_position[1], direction)
        if shot_result:
            shot_targets_locations.append(shot_result)
            matrix[shot_result[0]][shot_result[1]] = "."
            targets_shot += 1
    if targets_in_the_beginning == targets_shot:
        break

if targets_in_the_beginning == targets_shot:
    print(f"Training completed! All {targets_in_the_beginning} targets hit.")
else:
    print(f"Training not completed! {targets_in_the_beginning - targets_shot} targets left.")
for target in shot_targets_locations:
    print(target)
