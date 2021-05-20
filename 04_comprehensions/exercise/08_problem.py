names = input().split(", ")
data = {name: {} for name in names}

while True:
    command = input()
    if command == "End":
        break

    name, item, price = command.split("-")
    if item not in data[name]:
        data[name][item] = int(price)

[print(f"{name} -> Items: {len(data[name])}, Cost: {sum([data[name][item] for item in data[name]])}") for name in data]
