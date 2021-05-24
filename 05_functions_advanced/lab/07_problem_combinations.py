def combinations(data_, size_, combo_box=[]):
    if len(combo_box) == size_:
        print(*combo_box, sep=", ")
        return

    for i in range(len(data_)):
        combo_box.append(data_[i])
        combinations(data_[i + 1:], size_, combo_box)
        combo_box.pop()


data = input().split(", ")
size = int(input())
combinations(data, size)
