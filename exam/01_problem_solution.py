from collections import deque

chocolates = [int(i) for i in input().split(", ")]
cups_of_milk = deque([int(i) for i in input().split(", ")])
milkshakes = 0


def mix():
    chocolates.pop()
    cups_of_milk.popleft()


won = False
while chocolates and cups_of_milk:
    while chocolates[-1] <= 0:
        chocolates.pop()
        if not chocolates:
            break
    while cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        if not cups_of_milk:
            break
    if not cups_of_milk or not chocolates:
        break

    if chocolates[-1] == cups_of_milk[0]:
        mix()
        milkshakes += 1
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

    if milkshakes == 5:
        won = True
        break

if won:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join([str(i) for i in chocolates])}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join([str(i) for i in cups_of_milk])}")
else:
    print("Milk: empty")
