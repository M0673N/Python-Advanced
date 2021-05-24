def permute(text_, current_index=0):
    if current_index == len(text_):
        print("".join(text_))
        return

    for i in range(current_index, len(text_)):
        text_[current_index], text_[i] = text_[i], text_[current_index]
        permute(text_, current_index + 1)
        text_[current_index], text_[i] = text_[i], text_[current_index]


text = list(input())
permute(text)
