from collections import deque

bullet_price = int(input())
size_of_drum = int(input())
bullets = input().split()
locks = deque(input().split())
value = int(input())

drum = deque()


def reload():
    for i in range(size_of_drum):
        if bullets:
            drum.append(int(bullets.pop()))
        else:
            return True


reload()


def out_of_ammo():
    if not bullets:
        return True


while locks:
    if not drum and out_of_ammo():
        break
    elif drum:
        bullet = drum.popleft()
        value -= bullet_price
        if bullet <= int(locks[0]):
            locks.popleft()
            print("Bang!")
        else:
            print("Ping!")
        if not drum and not out_of_ammo():
            reload()
            print("Reloading!")
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(drum) + len(bullets)} bullets left. Earned ${value}")
