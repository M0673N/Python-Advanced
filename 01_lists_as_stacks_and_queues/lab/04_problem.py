from collections import deque

quantity_of_water = int(input())
queue = deque()
while True:
    command = input()

    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input().split()
    if command[0] == "End":
        print(f"{quantity_of_water} liters left")
        break
    elif command[0] == "refill":
        amount_to_refill = int(command[1])
        quantity_of_water += amount_to_refill
    else:
        liters_to_get = int(command[0])
        if quantity_of_water >= liters_to_get:
            quantity_of_water -= liters_to_get
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
