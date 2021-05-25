def recursive_power(number, power, result=1):
    if power == 0:
        return result

    result *= number
    data = recursive_power(number, power - 1, result)
    return data


# print(recursive_power(2, 10))
# print(recursive_power(10, 100))
