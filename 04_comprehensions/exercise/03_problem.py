countries = input().split(", ")
capitals = input().split(", ")
result = zip(countries, capitals)
[print(f"{pair[0]} -> {pair[1]}") for pair in result]
