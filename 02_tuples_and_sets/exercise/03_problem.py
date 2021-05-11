n = int(input())
elements = set()
for i in range(n):
    data = input().split()
    for element in data:
        elements.add(element)
for element in elements:
    print(element)
