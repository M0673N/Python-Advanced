from collections import deque

customers = deque([int(i) for i in input().split(", ")])
taxis = [int(i) for i in input().split(", ")]

total_time = 0
while customers:
    if not taxis:
        break

    if customers[0] <= taxis[-1]:
        total_time += customers[0]
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
elif not taxis:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(i) for i in customers])}")
