n = int(input())
odd = set()
even = set()
for i in range(1, n + 1):
    name = input()
    total = 0
    for letter in name:
        total += ord(letter)
    total //= i
    if total % 2 == 0:
        even.add(total)
    else:
        odd.add(total)

odd_sum = sum(odd)
even_sum = sum(even)

if odd_sum == even_sum:
    union = [str(i) for i in odd.union(even)]
    print(", ".join(union))
elif odd_sum > even_sum:
    difference = [str(i) for i in odd.difference(even)]
    print(", ".join(difference))
elif even_sum > odd_sum:
    symmetric_difference = [str(i) for i in odd.symmetric_difference(even)]
    print(", ".join(symmetric_difference))
