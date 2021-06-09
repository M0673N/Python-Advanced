n = int(input())
matrix = []
for i in range(n):
    matrix.append([i for i in input()])


def find_snake_position(data):
    for row_index in range(len(data)):
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] == "S":
                return [row_index, col_index]


def check_if_index_is_valid(row_, col_, data_):
    if 0 <= row_ <= len(data_) - 1 and 0 <= col_ <= len(data_[row_]) - 1:
        return True
    return False


def find_burrow_locations(data):
    locations = []
    for row_index in range(len(data)):
        for col_index in range(len(data[row_index])):
            if data[row_index][col_index] == "B":
                locations.append([row_index, col_index])
    return locations


consumed_food = 0
snake_position = find_snake_position(matrix)
burrow_positions = find_burrow_locations(matrix)
lost = False
while True:
    if consumed_food == 10:
        break

    command = input()

    if command == "up":
        if check_if_index_is_valid(snake_position[0] - 1, snake_position[1], matrix):
            if matrix[snake_position[0] - 1][snake_position[1]] == "*":
                consumed_food += 1
                matrix[snake_position[0] - 1][snake_position[1]] = "S"
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[0] -= 1
            elif matrix[snake_position[0] - 1][snake_position[1]] == "B":
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[0] -= 1
                if snake_position == burrow_positions[0]:
                    snake_position = burrow_positions[1]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "-"
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "S"
                elif snake_position == burrow_positions[1]:
                    snake_position = burrow_positions[0]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "S"
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "-"
            else:
                matrix[snake_position[0]][snake_position[1]] = "."
                matrix[snake_position[0] - 1][snake_position[1]] = "S"
                snake_position[0] -= 1
        else:
            matrix[snake_position[0]][snake_position[1]] = "."
            lost = True
            break

    elif command == "down":
        if check_if_index_is_valid(snake_position[0] + 1, snake_position[1], matrix):
            if matrix[snake_position[0] + 1][snake_position[1]] == "*":
                consumed_food += 1
                matrix[snake_position[0] + 1][snake_position[1]] = "S"
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[0] += 1
            elif matrix[snake_position[0] + 1][snake_position[1]] == "B":
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[0] += 1
                if snake_position == burrow_positions[0]:
                    snake_position = burrow_positions[1]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "."
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "S"
                elif snake_position == burrow_positions[1]:
                    snake_position = burrow_positions[0]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "S"
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "."
            else:
                matrix[snake_position[0]][snake_position[1]] = "."
                matrix[snake_position[0] + 1][snake_position[1]] = "S"
                snake_position[0] += 1
        else:
            matrix[snake_position[0]][snake_position[1]] = "."
            lost = True
            break

    elif command == "left":
        if check_if_index_is_valid(snake_position[0], snake_position[1] - 1, matrix):
            if matrix[snake_position[0]][snake_position[1] - 1] == "*":
                consumed_food += 1
                matrix[snake_position[0]][snake_position[1] - 1] = "S"
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[1] -= 1
            elif matrix[snake_position[0]][snake_position[1] - 1] == "B":
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[1] -= 1
                if snake_position == burrow_positions[0]:
                    snake_position = burrow_positions[1]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "."
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "S"
                elif snake_position == burrow_positions[1]:
                    snake_position = burrow_positions[0]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "S"
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "."
            else:
                matrix[snake_position[0]][snake_position[1]] = "."
                matrix[snake_position[0]][snake_position[1] - 1] = "S"
                snake_position[1] -= 1
        else:
            matrix[snake_position[0]][snake_position[1]] = "."
            lost = True
            break

    elif command == "right":
        if check_if_index_is_valid(snake_position[0], snake_position[1] + 1, matrix):
            if matrix[snake_position[0]][snake_position[1] + 1] == "*":
                consumed_food += 1
                matrix[snake_position[0]][snake_position[1] + 1] = "S"
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[1] += 1
            elif matrix[snake_position[0]][snake_position[1] + 1] == "B":
                matrix[snake_position[0]][snake_position[1]] = "."
                snake_position[1] += 1
                if snake_position == burrow_positions[0]:
                    snake_position = burrow_positions[1]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "."
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "S"
                elif snake_position == burrow_positions[1]:
                    snake_position = burrow_positions[0]
                    matrix[burrow_positions[0][0]][burrow_positions[0][1]] = "S"
                    matrix[burrow_positions[1][0]][burrow_positions[1][1]] = "."
            else:
                matrix[snake_position[0]][snake_position[1]] = "."
                matrix[snake_position[0]][snake_position[1] + 1] = "S"
                snake_position[1] += 1
        else:
            matrix[snake_position[0]][snake_position[1]] = "."
            lost = True
            break

if lost:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {consumed_food}")
for row in matrix:
    print("".join(row))
