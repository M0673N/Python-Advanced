rows = input().split("|")
matrix = [[char for char in row.split()] for row in rows]
result = [matrix[row_index][col_index] for row_index in range(len(rows) - 1, -1, -1) for col_index in
          range(len(matrix[row_index]))]
print(" ".join(result))
