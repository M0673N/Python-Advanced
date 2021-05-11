data = input().split()
m = int(data[0])
n = int(data[1])
m_set = set()
n_set = set()
for i in range(n):
    n_set.add(input())
for i in range(m):
    m_set.add(input())
result = n_set.intersection(m_set)
for item in result:
    print(item)
