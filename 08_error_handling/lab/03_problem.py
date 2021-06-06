text = input()
n = input()

try:
    print(text * int(n))
except ValueError:
    print("Variable times must be an integer")
