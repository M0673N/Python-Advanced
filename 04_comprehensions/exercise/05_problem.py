def sum_diagonal(data):
    data = sum([int(i) for i in data])
    return data


n = int(input())
matrix = [input().split(", ") for _ in range(n)]
first_diagonal = [matrix[row_index][col_index] for row_index in range(len(matrix)) for col_index in
                  range(len(matrix[row_index])) if row_index == col_index]
second_diagonal = [matrix[row_index][col_index] for row_index in range(len(matrix)) for col_index in
                   range(len(matrix[row_index])) if row_index + col_index == len(matrix) - 1]

print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum_diagonal(first_diagonal)}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum_diagonal(second_diagonal)}")
