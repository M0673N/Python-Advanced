def numbers_searching(*args):
    sorted_nums = sorted(list(set(args)))
    for i in range(len(sorted_nums) - 1):
        if not sorted_nums[i] + 1 == sorted_nums[i + 1]:
            missing = sorted_nums[i] + 1

    duplicates = set()
    for i in args:
        if args.count(i) > 1:
            duplicates.add(i)
    duplicates = sorted(list(duplicates))

    return [missing, duplicates]


# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
