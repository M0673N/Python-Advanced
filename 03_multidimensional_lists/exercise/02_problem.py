def read_matrix_2():
    rows, columns = map(int, input().split())
    data = []
    for row in range(rows):
        data.append([i for i in input().split()])
    return data


def count_2x2_squares_in_matrix(data):
    count = 0
    for row in range(len(data) - 1):
        for col in range(len(data[row]) - 1):
            if data[row][col] == data[row][col + 1] == data[row + 1][col] == data[row + 1][col + 1]:
                count += 1
    return count


matrix = read_matrix_2()
counter = count_2x2_squares_in_matrix(matrix)
print(counter)
