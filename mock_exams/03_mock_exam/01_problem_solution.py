from collections import deque


def check_for_special_case(data):
    result = []
    skip = False
    for num in data:
        if skip:
            skip = False
            continue
        if num % 25 == 0:
            skip = True
            continue
        else:
            result.append(num)
    return result


def try_to_match():
    matched = False
    if females[0] == males[-1]:
        males.pop()
        females.popleft()
        matched = True
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()
    return matched


def print_result(matches_, males_, females_):
    print(f"Matches: {matches_}")
    if not males_:
        print("Males left: none")
    else:
        print(f"Males left: {', '.join([str(i) for i in males_[::-1]])}")
    if not females_:
        print("Females left: none")
    else:
        print(f"Females left: {', '.join([str(i) for i in females_])}")


males = [int(i) for i in input().split() if int(i) > 0]
females = deque([int(i) for i in input().split() if int(i) > 0])
matches = 0

males = check_for_special_case(males)
females = deque(check_for_special_case(females))

while True:
    if not males or not females:
        break
    is_there_a_match = try_to_match()
    if is_there_a_match:
        matches += 1

print_result(matches, males, females)
