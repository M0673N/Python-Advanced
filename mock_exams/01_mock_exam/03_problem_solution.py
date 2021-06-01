from collections import deque


def flights(*args):
    data = deque(args)
    result = {}
    while not data[0] == "Finish":
        if data[0] not in result:
            destination = data.popleft()
            passengers = int(data.popleft())
            result[destination] = passengers
        else:
            destination = data.popleft()
            passengers = int(data.popleft())
            result[destination] += passengers
    return result


# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
