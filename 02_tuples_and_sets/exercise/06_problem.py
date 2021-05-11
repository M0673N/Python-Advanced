n = int(input())
longest = -1
winner = []
for i in range(n):
    data = [i.split(",") for i in input().split("-")]
    first_range_start = int(data[0][0])
    first_range_end = int(data[0][1])
    second_range_start = int(data[1][0])
    second_range_end = int(data[1][1])
    first_range = set(range(first_range_start, first_range_end + 1))
    second_range = set(range(second_range_start, second_range_end + 1))
    if len(first_range.intersection(second_range)) > longest:
        longest = len(first_range.intersection(second_range))
        winner = sorted(list(first_range.intersection(second_range)))

print(f"Longest intersection is {winner} with length {longest}")
