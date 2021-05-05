from collections import deque

circle = deque(input().split())
n = int(input())

counter = 1
while len(circle) > 1:
    if counter == n:
        print(f"Removed {circle.popleft()}")
        counter = 1
    else:
        circle.append(circle.popleft())
        counter += 1

print(f"Last is {circle[0]}")
