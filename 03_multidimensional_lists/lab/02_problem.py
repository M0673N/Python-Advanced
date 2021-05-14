rows, columns = map(int, input().split(", "))
matrix = []
for row in range(rows):
    matrix.append(list(map(int, input().split())))

for column in range(columns):
    column_sum = 0
    for row in range(rows):
        column_sum += matrix[row][column]
    print(column_sum)
