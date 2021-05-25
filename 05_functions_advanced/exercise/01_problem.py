data = map(int, input().split())
result = filter(lambda x: x % 2 == 0, data)
print(list(result))
