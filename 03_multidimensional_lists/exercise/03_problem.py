from sys import maxsize


def read_matrix_2():
    rows, columns = map(int, input().split())
    data = []
    for row in range(rows):
        data.append([int(i) for i in input().split()])
    return data


def find_biggest_3x3_sum(data):
    best_sum = -maxsize
    best_matrix = []
    for row in range(len(data) - 2):
        for col in range(len(data[row]) - 2):
            the_sum = []
            for small_matrix_row in range(3):
                for small_matrix_col in range(3):
                    the_sum.append(data[row + small_matrix_row][col + small_matrix_col])
            if sum(the_sum) > best_sum:
                best_sum = sum(the_sum)
                best_matrix.clear()
                for i in range(3):
                    row_to_be_added = []
                    for j in range(3):
                        row_to_be_added.append(the_sum.pop(0))
                    best_matrix.append(row_to_be_added)
    return best_sum, best_matrix


def print_small_matrix(data):
    for small_row in data:
        string_row = [str(i) for i in small_row]
        print(" ".join(string_row))


matrix = read_matrix_2()
maximum_sum, maximum_matrix = find_biggest_3x3_sum(matrix)
print(f"Sum = {maximum_sum}")
print_small_matrix(maximum_matrix)
