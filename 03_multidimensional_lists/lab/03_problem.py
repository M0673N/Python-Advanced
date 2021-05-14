n = int(input())
matrix = []
for row in range(n):
    matrix.append([int(i) for i in input().split()])

diagonal_sum = 0
for row in range(n):
    diagonal_sum += matrix[row][row]

print(diagonal_sum)
