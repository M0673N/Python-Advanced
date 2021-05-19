rows = int(input())
matrix = [input().split(", ") for i in range(rows)]
print([[int(item) for item in row if int(item) % 2 == 0] for row in matrix])
