from collections import deque

green_light = int(input())
free_window = int(input())
command = input()
queue = deque()
cars = 0
crash = False
while not command == "END":
    if command == "green":
        time_left_to_enter = green_light
        time_left_to_leave = free_window
        while queue:
            if time_left_to_enter > 0:
                for i in range(len(queue[0])):
                    if time_left_to_enter > 0:
                        time_left_to_enter -= 1
                    elif time_left_to_enter == 0 and time_left_to_leave > 0:
                        time_left_to_leave -= 1
                    elif time_left_to_leave == 0:
                        crash = True
                        hit_at = queue[0][i]
                        victim = queue[0]
                        break
                queue.popleft()
            elif time_left_to_enter == 0:
                break
            if not crash:
                cars += 1
            else:
                break
    else:
        queue.append(command)

    command = input()

if crash:
    print(f"A crash happened!")
    print(f"{victim} was hit at {hit_at}.")
else:
    print(f"Everyone is safe.")
    print(f"{cars} total cars passed the crossroads.")
