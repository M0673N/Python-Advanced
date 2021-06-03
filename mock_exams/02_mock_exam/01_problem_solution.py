from collections import deque


def remove_materials():
    firework_effects.popleft()
    explosive_powder.pop()


def print_result(data):
    if not data:
        print("Congrats! You made the perfect firework show!")
    else:
        print("Sorry. You can’t make the perfect firework show.")
    if firework_effects:
        print(f"Firework Effects left: {', '.join([str(i) for i in firework_effects])}")
    if explosive_powder:
        print(f"Explosive Power left: {', '.join([str(i) for i in explosive_powder])}")
    print(f"Palm Fireworks: {palms}")
    print(f"Willow Fireworks: {willows}")
    print(f"Crossette Fireworks: {crossettes}")


firework_effects = deque([int(i) for i in input().split(", ") if int(i) > 0])
explosive_powder = [int(i) for i in input().split(", ") if int(i) > 0]

palms = 0
willows = 0
crossettes = 0
failed = False

while True:
    if palms >= 3 and willows >= 3 and crossettes >= 3:
        break
    if not firework_effects or not explosive_powder:
        failed = True
        break

    firework = firework_effects[0] + explosive_powder[-1]
    if firework % 3 == 0 and not firework % 5 == 0:
        palms += 1
        remove_materials()
    elif firework % 5 == 0 and not firework % 3 == 0:
        willows += 1
        remove_materials()
    elif firework % 5 == 0 and firework % 3 == 0:
        crossettes += 1
        remove_materials()
    else:
        firework_effects[0] -= 1
        firework_effects.rotate(-1)

    if firework_effects:
        if firework_effects[0] == 0:
            firework_effects.popleft()

print_result(failed)
