data = input()
letters = {}
for letter in data:
    if letter not in letters:
        letters[letter] = 1
    else:
        letters[letter] += 1
letters = dict(sorted(letters.items(), key=lambda x: x))
for letter in letters:
    print(f"{letter}: {letters[letter]} time/s")
