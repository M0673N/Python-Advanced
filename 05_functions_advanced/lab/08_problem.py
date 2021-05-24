def expressions(nums_, current_sum=0, expression=""):
    if not nums_:
        return [(expression, current_sum)]

    plus_result = expressions(nums_[1:], current_sum + nums_[0], f"{expression}+{nums_[0]}")
    minus_result = expressions(nums_[1:], current_sum - nums_[0], f"{expression}-{nums_[0]}")
    return plus_result + minus_result


nums = list(map(int, input().split(", ")))
[print(f"{item[0]}={item[1]}") for item in expressions(nums)]
