data = (input().split())
occurrences = {}
for item in data:
    if item not in occurrences:
        occurrences[item] = 0
    occurrences[item] += 1

for item, occurrences in occurrences.items():
    print(f"{float(item)} - {occurrences} times")
