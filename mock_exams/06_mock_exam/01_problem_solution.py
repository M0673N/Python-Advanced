from collections import deque

bomb_effects = deque([int(i) for i in input().split(', ')])
bomb_casings = [int(i) for i in input().split(', ')]

datura = 40
cherry = 60
decoy = 120

datura_count = 0
cherry_count = 0
decoy_count = 0

won = False
while True:
    if datura_count >= 3 and cherry_count >= 3 and decoy_count >= 3:
        won = True
        break
    if not bomb_effects or not bomb_casings:
        break

    if bomb_effects[0] + bomb_casings[-1] == datura:
        datura_count += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == cherry:
        cherry_count += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == decoy:
        decoy_count += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if won:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(i) for i in bomb_effects])}")
if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(i) for i in bomb_casings])}")
print(f"Cherry Bombs: {cherry_count}")
print(f"Datura Bombs: {datura_count}")
print(f"Smoke Decoy Bombs: {decoy_count}")
