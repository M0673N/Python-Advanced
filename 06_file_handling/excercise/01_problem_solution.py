PUNCTUATION_MARKS = ["-", ",", ".", "!", "?"]


def read_file():
    with open("text.txt", "r") as file_:
        return file_.readlines()


def replace_symbols(row):
    for word_index in range(len(row)):
        for char_index in range(len(row[word_index])):
            if row[word_index][char_index] in PUNCTUATION_MARKS:
                row[word_index] = row[word_index][:char_index] + "@" + row[word_index][char_index + 1:]
    return row


def process_data(data):
    result = []
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
