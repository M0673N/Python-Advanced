n = int(input())
data = set()
for i in range(n):
    data.add(input())
data = set(sorted(data))  # "the order does not matter" - simply not true. If you don't sort you get 60/100.
for username in data:
    print(username)
