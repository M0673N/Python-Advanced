with open("numbers.txt", "r") as file:
    nums = map(int, file.readlines())
    print(sum(nums))
