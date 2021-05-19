start = int(input())
end = int(input())
result = list({num for num in range(start, end + 1) for divisor in range(2, 11) if num % divisor == 0})
print(result)
