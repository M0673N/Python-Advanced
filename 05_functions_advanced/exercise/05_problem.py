command = input()
data = list(map(int, input().split()))
if command == "Odd":
    odd_nums = filter(lambda x: x % 2 == 1, data)
    result = sum(odd_nums) * len(data)
else:
    even_nums = filter(lambda x: x % 2 == 0, data)
    result = sum(even_nums) * len(data)
print(result)
