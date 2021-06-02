from math import log

n = int(input())
base = input()

if base == "natural":
    result = log(n)
else:
    result = log(n, int(base))

print(f"{result:.2f}")
