def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for row in range(3, n + 1):
        row_to_append = [0] * row
        for num_index in range(len(row_to_append)):
            if num_index == 0:
                row_to_append[num_index] = triangle[-1][num_index]
            elif num_index == len(triangle[-1]):
                row_to_append[num_index] = triangle[-1][num_index - 1]
            else:
                row_to_append[num_index] = triangle[-1][num_index - 1] + \
                                           triangle[-1][num_index]
        triangle.append(row_to_append)
    return triangle


# print(get_magic_triangle(5))
