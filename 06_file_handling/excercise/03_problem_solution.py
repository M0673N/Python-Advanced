import os

while True:
    command = input()

    if command == "End":
        break

    command = command.split("-")
    file_name = command[1]

    if command[0] == "Create":
        file = open(file_name, "w")
        file.close()

    elif command[0] == "Add":
        content = command[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")

    elif command[0] == "Replace":
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                data = file.read()
                data = data.replace(old_string, new_string)
            with open(file_name, "w") as file:
                file.write(data)
        else:
            print("An error occurred")

    elif command[0] == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")
