def func_executor(*args):
    result = []
    for function_and_data in args:
        func = function_and_data[0]
        data = function_and_data[1]
        result.append(func(*data))
    return result


# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2
#
#
# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
