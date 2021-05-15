from collections import deque


def read_matrix_4():
    rows, columns = map(int, input().split())
    data = []
    for row in range(rows):
        data.append([0] * columns)
    return data


def move_snake(matrix_, snake_):
    snake_ = deque(snake_)
    for row in range(len(matrix_)):
        if row % 2 == 0:
            for col in range(len(matrix_[row])):
                matrix_[row][col] = snake_[0]
                snake_.rotate(-1)
        else:
            for col in range(len(matrix_[row]) - 1, -1, -1):
                matrix_[row][col] = snake_[0]
                snake_.rotate(-1)
    return matrix_


def print_result(data):
    for row in data:
        print("".join(row))


matrix = read_matrix_4()
snake = input()
matrix = move_snake(matrix, snake)
print_result(matrix)
