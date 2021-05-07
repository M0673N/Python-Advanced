from collections import deque

data = [i for i in input()]
left_brackets = deque([i for i in data if i in "[{("])
right_brackets = deque([i for i in data if i in "]})"])


def close_brackets():
    left_brackets.popleft()
    right_brackets.popleft()


def rotate():
    left_brackets.rotate(-1)
    right_brackets.rotate(-1)


def process_data():
    for i in range(len(left_brackets)):
        if left_brackets[0] == "(" and right_brackets[0] == ")":
            close_brackets()
        elif left_brackets[0] == "[" and right_brackets[0] == "]":
            close_brackets()
        elif left_brackets[0] == "{" and right_brackets[0] == "}":
            close_brackets()
        else:
            rotate()


def second_process():
    left = list(left_brackets)
    for i in range(len(left)):
        if left[-1] == "(" and right_brackets[0] == ")":
            left.pop()
            right_brackets.popleft()
        elif left[-1] == "[" and right_brackets[0] == "]":
            left.pop()
            right_brackets.popleft()
        elif left[-1] == "{" and right_brackets[0] == "}":
            left.pop()
            right_brackets.popleft()


process_data()
second_process()
if right_brackets:
    print("NO")
else:
    print("YES")
