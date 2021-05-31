import os
from pathlib import Path


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
    path = os.path.normpath(os.path.join(os.path.expanduser("~/Desktop"), "report.txt"))
    with open(path, 'w') as file:
        for extension in info:
            file.write(extension + "\n")
            for name in info[extension]:
                file.write(f"- - - {name}{extension}\n")


data = get_info()
deliver_result(data)
