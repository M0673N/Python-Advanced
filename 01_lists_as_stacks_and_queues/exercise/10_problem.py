from collections import deque

cups = deque([int(i) for i in input().split()])
bottles = [int(i) for i in input().split()]
waisted_water = 0

while cups:
    cup = cups[0]
    if bottles:
        while cup > 0:
            if bottles:
                cup -= bottles.pop()
            else:
                break
    else:
        break
    waisted_water += abs(cup)
    cups.popleft()

cups = [str(i) for i in cups]
bottles = [str(i) for i in bottles]

if cups:
    print(f"Cups: {' '.join(cups)}")
else:
    print(f"Bottles: {' '.join(bottles)}")
print(f"Wasted litters of water: {waisted_water}")
