import custom_package.custom_functions as func

current_sequence = [0, 1]
while True:
    command = input()

    if command == "Stop":
        break

    command, num = command.split()[0], int(command.split()[-1])
    current_sequence = func.process_data(command, current_sequence, num)
