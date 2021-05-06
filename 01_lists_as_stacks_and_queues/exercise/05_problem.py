from collections import deque

n = int(input())
circle = deque([])
distance_queue = deque([])
for i in range(n):
    info = input().split()
    fuel = int(info[0])
    distance = int(info[1])
    circle.append(fuel)
    distance_queue.append(distance)

rotations = 0
current_fuel = 0
original_circle = circle.copy()
original_distance_queue = distance_queue.copy()
started = False

while circle:
    if circle[0] + current_fuel >= distance_queue[0]:
        current_fuel += circle.popleft()
        current_fuel -= distance_queue.popleft()
        started = True
    else:
        if started:
            circle = original_circle.copy()
            distance_queue = original_distance_queue.copy()
            rotations += 1
            circle.rotate(-rotations)
            distance_queue.rotate(-rotations)
            started = False
            current_fuel = 0
            continue
        circle.rotate(-1)
        distance_queue.rotate(-1)
        rotations += 1

print(rotations)
