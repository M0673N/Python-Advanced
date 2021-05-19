vowels = ['a', 'o', 'u', 'e', 'i']
result = [i for i in input() if not i.lower() in vowels]
print("".join(result))
