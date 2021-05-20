categories = input().split(", ")
n = int(input())
bunker = {}
for category in categories:
    bunker[category] = {}
for i in range(n):
    category, item, quality_and_quantity = input().split(" - ")
    quantity, quality = quality_and_quantity.split(";")
    quality = int(quality.split(":")[1])
    quantity = int(quantity.split(":")[1])
    bunker[category][item] = [quality, quantity]

print(f"Count of items: {sum([sum([bunker[category][item][1] for item in bunker[category]]) for category in bunker])}")
print(f"Average quality: \
{sum([sum([bunker[category][item][0] for item in bunker[category]]) for category in bunker]) / len(bunker):.2f}")
"{category} -> {item1}, {item2}, …"
[print(f"{category} -> {', '.join([item for item in bunker[category]])}") for category in bunker]
