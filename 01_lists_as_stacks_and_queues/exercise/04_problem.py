box_of_clothes = [int(i) for i in input().split()]
rack_capacity = int(input())
clothes_value = 0
racks = 0
while box_of_clothes:
    item = box_of_clothes.pop()
    if clothes_value + item == rack_capacity:
        clothes_value = 0
        racks += 1
    elif clothes_value + item > rack_capacity:
        clothes_value = 0
        racks += 1
        clothes_value += item
    else:
        clothes_value += item

if clothes_value:
    racks += 1

print(racks)
