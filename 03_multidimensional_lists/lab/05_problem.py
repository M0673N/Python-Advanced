from sys import maxsize

rows, columns = map(int, input().split(", "))
matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

best_sum = -maxsize
best_position = []
for row in range(rows - 1):
    for col in range(columns - 1):
        the_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if the_sum > best_sum:
            best_sum = the_sum
            best_position = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

print(f"{best_position[0][0]} {best_position[0][1]}")
print(f"{best_position[1][0]} {best_position[1][1]}")
print(best_sum)
