def list_manipulator(nums, *args):
    args = list(args)
    if args:
        if args[0] == "add":
            if args[1] == "beginning":
                nums = args[2:] + nums
            elif args[1] == "end":
                nums.extend(args[2:])
        elif args[0] == "remove":
            if args[1] == "beginning":
                if len(args) == 3:
                    for i in range(args[2]):
                        nums.pop(0)
                else:
                    nums.pop(0)
            elif args[1] == "end":
                if len(args) == 3:
                    for i in range(args[2]):
                        nums.pop()
                else:
                    nums.pop()
    return nums


# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
# print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
