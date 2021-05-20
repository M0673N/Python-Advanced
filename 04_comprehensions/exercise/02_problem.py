data = input().split(", ")
result = [f"{word} -> {len(word)}" for word in data]
print(", ".join(result))
