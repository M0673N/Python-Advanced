def print_triangle(num):
    for i in range(num):
        for j in range(i):
            print(j + 1, end=" ")
        print()
    for i in range(num, -1, -1):
        for j in range(i):
            print(j + 1, end=" ")
        print()


def math_operations(data):
    if data.split()[1] == "^":
        return float(data.split()[0]) ** int(data.split()[2])
    return eval(data)


def get_fibonacci_nums(num):
    num_1 = 0
    num_2 = 1
    result = [num_1, num_2]
    if num == 1:
        return "0"
    elif num == 2:
        return result
    else:
        for i in range(num - 2):
            num_3 = num_1 + num_2
            num_1 = num_2
            num_2 = num_3
            result.append(num_3)
        return result


def process_data(command, sequence, num):
    if command == "Create":
        sequence = get_fibonacci_nums(num)
        print(" ".join([str(i) for i in sequence]))
        return sequence
    elif command == "Locate":
        if num in sequence:
            print(f"The number - {num} is at index {sequence.index(num)}")
        else:
            print(f"The number {num} is not in the sequence")
