import os


def create_file(file_name):
    file = open(file_name, "w")
    file.close()


def add_info(file_name, content):
    with open(file_name, "a") as file:
        file.write(content + "\n")


def replace_info(file_name, old_string, new_string):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = file.read()
            data = data.replace(old_string, new_string)
        with open(file_name, "w") as file:
            file.write(data)
    else:
        print("An error occurred")


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("An error occurred")


actions = {"Create": create_file, "Add": add_info, "Replace": replace_info, "Delete": delete_file}

while True:
    command = input()

    if command == "End":
        break

    args = command.split("-")
    action = args.pop(0)
    actions[action](*args)
