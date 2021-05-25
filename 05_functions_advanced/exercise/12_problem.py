def palindrome(word, index, first_half=[], second_half=[]):
    if index == len(word) // 2:
        if first_half == second_half:
            return f"{word} is a palindrome"
        else:
            return f"{word} is not a palindrome"

    first_half.append(word[index])
    second_half.append(word[-(index + 1)])

    data = palindrome(word, index + 1, first_half, second_half)
    return data


# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))
