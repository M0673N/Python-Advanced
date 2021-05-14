n = int(input())
matrix = []
for row in range(n):
    matrix.append([i for i in input()])

symbol = input()
is_found = False

for row in range(n):
    if is_found:
        break
    for col in range(len(matrix[row])):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            is_found = True
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
