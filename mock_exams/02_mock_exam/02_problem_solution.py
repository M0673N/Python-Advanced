n = int(input())


def create_field(size):
    field_ = []
    for i in range(size):
        field_.append(input().split())
    return field_


def locate_player(field_):
    for row_index in range(len(field_)):
        for col_index in range(len(field_[row_index])):
            if field_[row_index][col_index] == "P":
                return [row_index, col_index]


def move_player(location, field_, command_, coins_=0):
    failed_ = False
    if command_ == "up":
        if location[0] - 1 >= 0:
            location[0] -= 1
        else:
            failed_ = True
            return location, failed_, coins_
    elif command_ == "down":
        if location[0] + 1 < len(field_):
            location[0] += 1
        else:
            failed_ = True
            return location, failed_, coins_
    elif command_ == "left":
        if location[1] - 1 >= 0:
            location[1] -= 1
        else:
            failed_ = True
            return location, failed_, coins_
    elif command_ == "right":
        if location[1] + 1 < len(field_[location[0]]):
            location[1] += 1
        else:
            failed_ = True
            return location, failed_, coins_

    if field_[location[0]][location[1]] == "X":
        failed_ = True
        return location, failed_, coins_
    elif field_[location[0]][location[1]].isdigit():
        coins_ = int(field_[location[0]][location[1]])

    return location, failed_, coins_


failed = False
field = create_field(n)
position = locate_player(field)
coins = 0
path = []
while True:
    if coins >= 100:
        break
    command = input()
    position, failed, coins_to_be_added = move_player(position, field, command)
    if failed:
        break
    # if coins_to_be_added:
    #     path.append(f"[{position[0]}, {position[1]}]")
    '''What if you collect 0 coins? 
    The description says: "The field positions from which the player has collected coins as lists"'''
    path.append(f"[{position[0]}, {position[1]}]")
    coins += coins_to_be_added

if failed:
    print(f"Game over! You've collected {coins // 2} coins.")
else:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")
for pos in path:
    print(pos)
