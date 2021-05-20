rows, cols = map(int, input().split())
result = [[chr(row + 97) + chr(row + col + 97) + chr(row + 97) for col in range(cols)] for row in range(rows)]
[print(" ".join(row)) for row in result]
