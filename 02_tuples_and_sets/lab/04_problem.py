n = int(input())
cars = set()
for i in range(n):
    command, plate = input().split(", ")
    if command == "IN":
        cars.add(plate)
    else:
        cars.remove(plate)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
