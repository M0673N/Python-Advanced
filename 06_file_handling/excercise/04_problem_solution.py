import os


def get_info():
    files = {}
    for filename in os.listdir():
        if os.path.isfile(filename):
            name, extension = os.path.splitext(filename)
            if extension not in files:
                files[extension] = [name]
            else:
                files[extension].append(name)
    files = dict(sorted(files.items(), key=lambda x: (x[0], x[1])))
    return files


def deliver_result(info):
    username = os.getlogin()
    with open(f'C:\\Users\\{username}\\Desktop\\report.txt', 'w') as file:
        for extension in info:
            file.write(extension + "\n")
            for name in info[extension]:
                file.write(f"- - - {name}{extension}\n")


data = get_info()
deliver_result(data)
