n = int(input())
info = []
for i in range(n):
    info.append(input())

[print(i) for i in set(info)]
