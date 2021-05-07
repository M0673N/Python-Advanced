from collections import deque

data = input().split(";")
starting_time = input().split(":")
seconds = int(starting_time[0]) * 60 * 60 + int(starting_time[1]) * 60 + int(starting_time[2])
robots = deque()

command = input()
for i in range(len(data)):
    robot = data[i].split("-")
    name = robot[0]
    processing = int(robot[1])
    robots.append([name, 0, processing])


def convert():
    internal_seconds = seconds
    hours = internal_seconds // 3600
    internal_seconds -= hours * 3600
    minutes = internal_seconds // 60
    internal_seconds -= minutes * 60
    secs = internal_seconds
    if hours >= 24:
        hours -= 24
    time = f"[{hours:02}:{minutes:02}:{secs:02}]"
    return time


products = deque()
while not command == "End":
    products.append(command)
    command = input()

while products:
    seconds += 1
    for r in range(len(robots)):
        if robots[r][1] <= seconds:
            robots[r][1] = robots[r][2] + seconds
            print(f"{robots[r][0]} - {products.popleft()} {convert()}")
            break
    else:
        products.rotate(-1)
