from collections import deque

food_amount = int(input())
orders = [int(i) for i in input().split()]
biggest_order = max(orders)
orders = deque(orders)
failed = False

print(biggest_order)

while orders:
    next_in_line = orders.popleft()
    if food_amount < next_in_line:
        print(f"Orders left: ", end="")
        print(next_in_line, end=" ")
        while orders:
            print(orders.popleft(), end=" ")
        failed = True
        break
    else:
        food_amount -= next_in_line

if not failed:
    print("Orders complete")
