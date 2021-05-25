data = list(map(int, input().split()))
positive_nums_sum = sum(filter(lambda x: x >= 0, data))
negative_nums_sum = sum(filter(lambda x: x < 0, data))
print(negative_nums_sum)
print(positive_nums_sum)

if positive_nums_sum > abs(negative_nums_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")
