test = input()
indexes_of_opening_parenthesis = []
for i in range(len(test)):
    if test[i] == "(":
        indexes_of_opening_parenthesis.append(i)
    elif test[i] == ")":
        end = i + 1
        start = indexes_of_opening_parenthesis.pop()
        print(test[start:end])
