result = {}
with open("words.txt", "r") as file:
    words = []
    for line in file.readlines():
        for word in line.split():
            words.append(word)

with open("text2.txt", "r") as file:
    text = file.readlines()
    for word in words:
        result[word] = 0
        for row in text:
            if word in row.lower():
                result[word] += 1

result = dict(sorted(result.items(), key=lambda x: -x[1]))

with open("output.txt", "w") as file:
    for item in result:
        file.write(f"{item} - {result[item]}\n")
