command = input()
phonebook = {}
while not command.isdigit():
    command = command.split("-")
    name = command[0]
    number = command[1]
    phonebook[name] = number
    command = input()
for i in range(int(command)):
    person_to_check = input()
    if person_to_check in phonebook:
        print(f"{person_to_check} -> {phonebook[person_to_check]}")
    else:
        print(f"Contact {person_to_check} does not exist.")
