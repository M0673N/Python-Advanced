import re

punctuation_marks_pattern = r"[/./?/!,-]"


def read_file():
    with open("text.txt", "r") as file_:
        return file_.readlines()


def process_data(data):
    result = []

    def replace_symbols(row_):
        for word_index in range(len(row_)):
            row_[word_index] = re.sub(punctuation_marks_pattern, "@", row_[word_index])
        return row_

    for row_index in range(len(data)):
        if row_index % 2 == 0:
            row = list(reversed(data[row_index].split()))
            processed_row = replace_symbols(row)
            result.append(" ".join(processed_row))
    return result


def print_result(data):
    for row in data:
        print(row)


file = read_file()
processed_data = process_data(file)
print_result(processed_data)
