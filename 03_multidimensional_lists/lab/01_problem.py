size = input().split(", ")
rows = int(size[0])
columns = int(size[1])
matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

matrix_sum = 0
for row in matrix:
    matrix_sum += sum(row)

print(matrix_sum)
print(matrix)
