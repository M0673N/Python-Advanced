rows = int(input())
matrix = [input().split(", ") for i in range(rows)]
print([int(item) for row in matrix for item in row])
