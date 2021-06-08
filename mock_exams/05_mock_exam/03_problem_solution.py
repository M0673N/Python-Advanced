from collections import deque


def best_list_pureness(list_of_nums, rotations):
    list_of_nums = deque(list_of_nums)

    def calculate_pureness(list_of_nums_):
        result_ = 0
        for num_index in range(len(list_of_nums_)):
            result_ += list_of_nums_[num_index] * num_index
        return result_

    highest_pureness = calculate_pureness(list_of_nums)
    list_of_pureness_results = [highest_pureness]
    for i in range(rotations):
        list_of_nums.rotate(1)
        pureness = calculate_pureness(list_of_nums)
        list_of_pureness_results.append(pureness)
        if pureness > highest_pureness:
            highest_pureness = pureness
    rotations = 0
    for pureness_result in list_of_pureness_results:
        if not pureness_result == max(list_of_pureness_results):
            rotations += 1
        else:
            break

    return f"Best pureness {highest_pureness} after {rotations} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)
