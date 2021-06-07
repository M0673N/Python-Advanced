n = int(input())
matrix = []
for row in range(n):
    matrix.append([0] * n)

n_bombs = int(input())
bomb_locations = []
for i in range(n_bombs):
    row, col = input()[1:-1].split(", ")
    location = (int(row), int(col))
    bomb_locations.append(location)

for position in bomb_locations:
    row = position[0]
    col = position[1]
    matrix[row][col] = "*"

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] != "*":
            if col_index - 1 >= 0 and matrix[row_index][col_index - 1] == "*":
                matrix[row_index][col_index] += 1
            if col_index + 1 <= len(matrix[row_index]) - 1 and matrix[row_index][col_index + 1] == "*":
                matrix[row_index][col_index] += 1
            if row_index - 1 >= 0 and matrix[row_index - 1][col_index] == "*":
                matrix[row_index][col_index] += 1
            if row_index + 1 <= len(matrix) - 1 and matrix[row_index + 1][col_index] == "*":
                matrix[row_index][col_index] += 1
            if row_index - 1 >= 0 and col_index - 1 >= 0 and matrix[row_index - 1][col_index - 1] == "*":
                matrix[row_index][col_index] += 1
            if row_index + 1 <= len(matrix) - 1 and col_index - 1 >= 0 and matrix[row_index + 1][col_index - 1] == "*":
                matrix[row_index][col_index] += 1
            if row_index - 1 >= 0 and col_index + 1 <= len(matrix[row_index]) - 1 and \
                    matrix[row_index - 1][col_index + 1] == "*":
                matrix[row_index][col_index] += 1
            if row_index + 1 <= len(matrix) - 1 and col_index + 1 <= len(matrix[row_index]) - 1 and \
                    matrix[row_index + 1][col_index + 1] == "*":
                matrix[row_index][col_index] += 1

for row in matrix:
    row = [str(i) for i in row]
    print(' '.join(row))
