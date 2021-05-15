def read_matrix():
    n = int(input())
    data = []
    for row in range(n):
        data.append([int(i) for i in input().split()])
    return data


def find_primary_diagonal(data):
    diagonal_values = []
    for row in range(len(data)):
        diagonal_values.append(data[row][row])
    return sum(diagonal_values)


def find_secondary_diagonal(data):
    diagonal_values = []
    for row in range(len(data) - 1, -1, -1):
        col = len(data) - 1 - row
        diagonal_values.append(data[row][col])
    return sum(diagonal_values)


matrix = read_matrix()
primary_diagonal = find_primary_diagonal(matrix)
secondary_diagonal = find_secondary_diagonal(matrix)
print(abs(primary_diagonal - secondary_diagonal))
