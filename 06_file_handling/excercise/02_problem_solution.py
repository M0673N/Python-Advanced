from string import punctuation
from string import ascii_letters


def read_file():
    with open("text.txt", "r") as file_:
        result = []
        for row_ in file_.readlines():
            result.append(row_.strip())
    return result


def count_punctuation_marks_and_letters(data):
    result = []
    for row in data:
        punctuation_marks_count = len([symbol for symbol in row if symbol in punctuation])
        letters_count = len([symbol for symbol in row if symbol in ascii_letters])
        result.append(f"({letters_count})({punctuation_marks_count})")
    return result


def write_result_to_file(data, info):
    with open("output.txt", "w") as file_:
        for row_index in range(len(data)):
            file_.write(f"Line {row_index + 1}: {data[row_index]} {info[row_index]}\n")


file = read_file()
lines_info = count_punctuation_marks_and_letters(file)
write_result_to_file(file, lines_info)
